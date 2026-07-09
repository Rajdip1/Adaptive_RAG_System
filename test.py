# import langchain
# import transformers
# import fastapi

# print(langchain.__version__)
# print(transformers.__version__) 
# print(fastapi.__version__) 

from qdrant_client import QdrantClient

# Test connection
client = QdrantClient(
    url="https://85fe5c16-4231-4706-acda-6bed31a65868.eu-central-1-0.aws.cloud.qdrant.io",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwic3ViamVjdCI6ImFwaS1rZXk6YWIxYzMzMjMtMTA0Ny00OTg0LWE1ZGYtZTRlNjBhYzc2Y2I3In0.BYacySwU3xtjVr2ah1O1qhEnqjq8peADL5K_gSKKh9g"
)

# List collections
collections = client.get_collections()
print("Connected successfully!")
print(f"Collections: {collections}")
