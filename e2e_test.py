import unittest


from db import Db as dbrepo
from blobRepo import BlobRepo as blobs


class E2ETests(unittest.TestCase):

    def test_getblob(self):
        
        db = dbrepo()
        blob_repo = blobs()

        #this would actually be the docids passed in
        docids_test = [1,2,3,4]

        datafiles = list(blob_repo.GetBlobs(db.get_documentnames_by_docid(docids_test)))    

        self.assertTrue(len(datafiles) == len(docids_test))




if __name__ == "__main__":
    unittest.main()


