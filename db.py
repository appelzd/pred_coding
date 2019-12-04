
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

    def save_similar_docids(self, search_id, docids):
        
        sql_con = pyodbc.connect(Configuration.GetDbConnectionString())
        tmp = topic.split('+')
                    
        cursor = sql_con.cursor()
     
        cursor.execute('INSERT INTO Topics(name) values(?)', topic)
        
        curse = cursor.execute('select @@IDENTITY') 
        id = curse.fetchval()
        
        for t in tmp:
            a = t.split('"') 
            cursor.execute('INSERT INTO TopicWords(TopicId ,name, weight) values(?,?, ?)', id, a[1], a[0][:-1])    

        sql_con.commit()
        cursor.close()
        sql_con.close()