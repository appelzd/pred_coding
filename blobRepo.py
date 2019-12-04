import os, uuid
from azure.storage.blob import BlockBlobService, PublicAccess

from config import Configuration

class BlobRepo:

    def GetBlobs(self, doc_names):
        try:
            block_blob_service = BlockBlobService(account_name=Configuration.GetAzureBlobAccountName(), account_key=Configuration.GetAzureBlobKey())
            blobs = block_blob_service.list_blobs(Configuration.GetBlobContainerName())

            for b in doc_names:                
                try:
                    print(b.name)
                    bt = block_blob_service.get_blob_to_text(Configuration.GetBlobContainerName(), b.name)
                    yield bt.content
                except Exception as ex:
                    print('failed opening docs')
                    print(ex)
                    continue
        except Exception as e:
            print('Failed retrieving docs')
            print(e)
