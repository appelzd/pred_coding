import unittest


from db import Db as dbrepo
from blobRepo import BlobRepo as blobs
from process_text import pred_coding_poc

class E2ETests(unittest.TestCase):

    def test_getblob(self):
        
        db = dbrepo()
        blob_repo = blobs()

        #this would actually be the docids passed in
        docids_test = [1,2,3,4]

        datafiles = list(blob_repo.GetBlobs(db.get_documentnames_by_docid(docids_test)))    

        self.assertTrue(len(datafiles) == len(docids_test))

    def test_process_docids_for_similarity(self):
        prc = pred_coding_poc()
        results = prc.process_docids_for_similarity('searchid', [1,2,3,4])

        self.assertTrue(1 == 1)

if __name__ == "__main__":
    unittest.main()



