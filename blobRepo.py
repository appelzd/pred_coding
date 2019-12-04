import os, uuid
from azure.storage.blob import BlockBlobService, PublicAccess

from config import Configuration

class BlobRepo:

    def GetBlobs(self, doc_names):
        try:
            block_blob_service = BlockBlobService(account_name=Configuration.GetAzureBlobAccountName(), account_key=Configuration.GetAzureBlobKey())
            
            blobs = []
            if len(doc_names) > 0:
                blobs = doc_names
            else:
                temp = block_blob_service.list_blobs(Configuration.GetBlobContainerName())
                blobs = list([x.name for x in temp]) 

            for b in blobs:                
                try:
                    print(b)
                    bt = block_blob_service.get_blob_to_text(Configuration.GetBlobContainerName(), b)
                    yield (b, bt.content)
                except Exception as ex:
                    print('failed opening docs')
                    print(ex)
                    continue
        except Exception as e:
            print('Failed retrieving docs')
            print(e)
