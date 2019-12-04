import unittest

import db

class db_test_class(unittest.TestCase):

    def test_get_documents_by_docid(self):
        repo = db.Db()

        docids = [1,2,3,4]
        results = repo.get_documentnames_by_docid(docids)

        self.assertTrue(len(results) == 4)

    def test_save_similar_docids(self):
        self.assertTrue(1)


if __name__ == "__main__":
    unittest.main()