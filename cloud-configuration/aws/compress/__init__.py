import logging
import base64

import gzip
import azure.functions as func
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


# src: https://docs.microsoft.com/en-us/python/api/overview/azure/storage-blob-readme?view=azure-python


############### HTTP body input example
#     {
#         "blob_name":"name of file",         
#         "overwrite": True/False,
#         "data":"base64_encoded_data"
#     }





fileName = ""
fileExtCompress = ".gz"
fileDir = "/tmp/"
# connection string to the storage account
connect_str = "DefaultEndpointsProtocol=https;AccountName=storageaccountnameofradon83f0;AccountKey=NSZ+aGSyRfjM9jCcBQ==;EndpointSuffix=core.windows.net"
my_new_container_name = "first-container-using-py"

def write_to_file(save_path, data):
  with open(save_path, "wb") as f:
    f.write(base64.b64decode(data))

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    

    ## Create a new container if required
    # Get the container client from the connection string
    # container_client = ContainerClient.from_connection_string(conn_str=connect_str, container_name=my_new_container_name)
    # # create a container named <my_new_container_name>
    # container_client.create_container()

    img = req.params.get('data')
    if not img:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            img = req_body.get('data')

    if img:
        fileName = req.get_json().get('blob_name')

        # Write the base64 data to image file 
               
        write_to_file(fileDir+fileName, img)

        # write the code to compress the image                
        with open(fileDir+fileName, "rb") as file_in:
            # Open output file.            
            with gzip.open(fileDir+fileName+fileExtCompress, "wb") as file_out:
                # Write output in compressed.
                file_out.writelines(file_in)

        # code to write the file to blob storage
        # blob name should be unique        
        blob = BlobClient.from_connection_string(conn_str=connect_str, container_name=my_new_container_name, blob_name=fileName+fileExtCompress)

        
        with open(fileDir+fileName+fileExtCompress, "rb") as data:
            blob.upload_blob(data, overwrite=True)
        
        return func.HttpResponse(f"{req.get_json().get('blob_name')} file is compressed and stored in {my_new_container_name} container.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
