import os, uuid

#this is the library that interacts with blob storage
from azure.storage.blob import BlockBlobService, PublicAccess

from config import Configuration

class BlobRepo:

    def GetBlobs(self, doc_names):
        try:
            # connect with azure blob
            block_blob_service = BlockBlobService(account_name=Configuration.GetAzureBlobAccountName(), account_key=Configuration.GetAzureBlobKey())
            
            blobs = []

            # if we send in docnames, return only those docs
            # otherwise return all the docs
            if len(doc_names) > 0:
                blobs = doc_names
            else:
                temp = block_blob_service.list_blobs(Configuration.GetBlobContainerName())
                blobs = list([x.name for x in temp]) 

            for b in blobs:                
                try:
                    print(b)
                    # opens the blob and returns the text
                    bt = block_blob_service.get_blob_to_text(Configuration.GetBlobContainerName(), b)
                    
                    # fucntions as a generator
                    yield (b, bt.content)
                except Exception as ex:
                    print('failed opening docs')
                    print(ex)
                    continue
        except Exception as e:
            print('Failed retrieving docs')
            print(e)
