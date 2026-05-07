from azure.storage.blob import BlobServiceClient

# Replace with your actual connection string from Azure Portal
connection_string = "DefaultEndpointsProtocol=https;AccountName=<your_account_name>;AccountKey=<your_account_key>;EndpointSuffix=core.windows.net"

# Replace with your container and blob names
container_name = "sample-container"
blob_name = "testfile.txt"

def test_blob_connection():
    try:
        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # Get container client
        container_client = blob_service_client.get_container_client(container_name)

        # List blobs in the container
        print("Listing blobs in container:")
        for blob in container_client.list_blobs():
            print(f"- {blob.name}")

        # Download a blob