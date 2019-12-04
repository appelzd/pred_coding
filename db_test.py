import unittest

import db

class db_test_class(unittest.TestCase):

    def test_get_documents_by_docid(self):
        repo = db.Db()

        docids = [1,2,3,4]
        results = repo.get_documentnames_by_docid(docids)

        self.assertTrue(len(results) == 4)

    def test_save_similar_docids(self):
        repo = db.Db()

        doc_names = dict()
        doc_names[2] = 'CAT0000002.txt'
        doc_names[3] = 'CAT0000017.txt'
        doc_names[4] = 'CAT0000021.txt'
        doc_names[5] = 'CAT0000026.txt'
        doc_names[6] = 'CAT0000027.txt'
        
        repo.save_similar_docids( 'first', [1,2,3], list(map( lambda x: doc_names[x] ,doc_names)))
        
        self.assertTrue(1)

    def test_getdocids_for_docnames_returns_docids(self):
        doc_names = dict()
        doc_names[2] = 'CAT0000002.txt'
        doc_names[3] = 'CAT0000017.txt'
        doc_names[4] = 'CAT0000021.txt'
        doc_names[5] = 'CAT0000026.txt'
        doc_names[6] = 'CAT0000027.txt'
        
        repo = db.Db()
        result = repo.get_docids_for_docnames(list(map( lambda x: doc_names[x] ,doc_names)))

        for k in result:
            print(k)
            print(doc_names[k])
            self.assertTrue(doc_names[k] is not None)

if __name__ == "__main__":
    unittest.main()