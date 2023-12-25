from openai import OpenAI
api_key = "sk-v568f6yv9867yvboiub7trd7654seiy8uvi8"     # change with your openai api key
client = OpenAI(api_key=api_key)

# Creating an embedding for the query
query_response = client.embeddings.create(
    input="What is my Banana?",    # change to be a query relating to your data
    model="text-embedding-ada-002"
)

# Extracting the query vector
query_vector = query_response.data[0].embedding

# Querying the Pinecone index
query_result = index.query(
  vector=query_vector,
  top_k=1,                     # This will only show the most relevant piece of data, to show more increase 1 to the desired number of results
  include_values=True         # This will show the metadata of data stored
)

# Accessing metadata from the query result
if query_result['matches']:
    match = query_result['matches'][0]
    query_id = match['id']

    # Fetch the response from Pinecone using the obtained ID
    fetch_response = index.fetch(ids=[query_id])

    # Extract the metadata from the fetched response
    query_metadata = fetch_response['vectors'][query_id]['metadata']
    query_meta = query_metadata.get('label', 'Unknown')  # change label to the label you give metadata 
                                                        # Default to 'Unknown' if 'label' is not found
    print(f"{query_meta}")
else:
    print("No matches found.")
