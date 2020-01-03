class Configuration:
    @staticmethod
    def GetBlobContainerName():
        #return 'chaucer'
        return 'test'
    
    @staticmethod
    def GetDbConnectionString():
        return 'DRIVER={ODBC Driver 17 for SQL Server};Server=tcp:csdev.database.windows.net,1433;Database=;Trusted_Connection=no;UID=;Pwd='


    @staticmethod
    def GetAzureBlobAccountName():
        return 'topicmodeling7885000326'

    @staticmethod
    def GetAzureBlobKey():
        return 'XcdfPfvBQVgt0g+h3voFQ7ySystcnrJTsEQc73clWmsWuSzFFw6b5v89pO6idc7JyyUlefvC6bIV9QABluMBhA=='
    