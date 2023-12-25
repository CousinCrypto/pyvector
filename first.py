from openai import OpenAI
api_key = "sk-fv75t8f6yufc54e7f7iyg9658figyv568fyg80"  #change with your api key 
client = OpenAI(api_key=api_key)

# Creating an embedding
response = client.embeddings.create(
    input="My Banana is tall",    # change input to the data you want to vector embed & store in vector database
    model="text-embedding-ada-002"
)

# Extracting the vector
vector = response.data[0].embedding
print(vector)

# Preparing ids and vecs for upsert
ids = ["1"]  # the ID number in the vector database (change everytime/autoincrement as cant share ID)
vecs = [vector]  
metadata = [{"Meta": "My Banana is tall"}]  # change input to the data you want to store as metadata & store in vector database

# Creating and updating the Pinecone index
index = pinecone.Index('langpine')
index.upsert(vectors=zip(ids, vecs, metadata))

print("Vector upload complete.")
