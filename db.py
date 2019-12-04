
import pandas
import pyodbc
from config import Configuration

class Db:

    def get_documentnames_by_docid(self, docids):
        sql_con = pyodbc.connect(Configuration.GetDbConnectionString())
        
        cursor = sql_con.cursor()
        docid_string = 'SELECT TextPath FROM Document WHERE Docid in ('
        for i in docids:
            docid_string += str(i)
            docid_string += ','

        docid_string = docid_string.strip(',')
        docid_string += ')'

        print(docid_string)
        cursor.execute(docid_string)

        rtn = cursor.fetchmany(len(docids))

        cursor.close()
        sql_con.close()
        
        return list([x[0].rpartition('\\')[2] for x in rtn])

    def save_similar_docids(self, search_uid, search_docids, similar_docs):
        
        sql_con = pyodbc.connect(Configuration.GetDbConnectionString())
                    
        cursor = sql_con.cursor()
     
        cursor.execute('INSERT INTO zDocumentSimilarity_Models(SearchDocids,SearchIdentifier) values(?,?)', search_uid, self.strigify_docids(search_docids))
        
        curse = cursor.execute('select @@IDENTITY') 
        id = curse.fetchval()
        
        similar_docids_string = self.get_docids_for_docnames(similar_docs)
        cursor.execute('INSERT INTO zDocumentSimilarity_DocumentMatches(ModelId , SimilarDocids) values(?,?)', id, self.strigify_docids(similar_docids_string))    

        sql_con.commit()
        cursor.close()
        sql_con.close()

    # this is an incredibly inefficient way to get the docids from the names
    # in a prod situation, we would want to do this differently
    def get_docids_for_docnames(self, similar_docs):
        sql_con = pyodbc.connect(Configuration.GetDbConnectionString())
        rtn = list()

        # i forgot  that i was going to add how close it was to a topic
        # the tuple here has that info, but the db doesn't have a column
        for i in similar_docs:
            cursor = sql_con.cursor()
            docid_string = 'select DocId from Document where TextPath like \'%'
            docid_string += i[0]
            docid_string += '\''

            print(docid_string)
            cursor.execute(docid_string)

            #this is a row, so we want the 1st col
            id = cursor.fetchone()
            if id is not None:
                rtn.append(id)    
            
            cursor.close()
        sql_con.close()

        return list(x[0] for x in rtn)

    def strigify_docids(self, ids):
        docid_string = '(\')'
        for i in ids:
            docid_string += str(i)
            docid_string += ','

            docid_string = docid_string.strip(',')
            docid_string += '\')'

        return docid_string