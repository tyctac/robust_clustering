from pymongo import MongoClient

class MongoOper:
    def __init__(self):
        self.client = MongoClient()
        self.db = object()
        self.setdb('cluster')
        self.dbauth('clust','cluster')

    def setdb(self,dbname):
        self.db = self.client[dbname]

    def dbauth(self,uname,upasswd):
        self.db.authenticate(uname,upasswd)
