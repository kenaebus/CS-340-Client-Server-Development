from pymongo import MongoClient
from bson.objectid import ObjectId

class animalShelter(object):
    def __init__(self,USER,PASS):
        
        USER = 'aacuser'
        PASS = 'root123'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31741
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

        print("Connection Successful")
    
    def create(self, data):
        if data is not None:
            print(data)
            create = self.collection.insert_one(data) # data should be dictionary
            if create != 0:
                print("Successful")
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, data):
        if data:
            result = self.collection.find(data, {"id": False})
            print(result)
        else:
            result = self.collection.find({}, {"id": False})
        return list(result)
        
    def update(self, prevData, newData):
        if prevData is not None: 
            if self.collection.count_documents(prevData)!=0:
                result = self.collection.update_many(prevData, {"$set": newData})
                updated = result.raw_result
                print("Updated")
            else:
                updated = "Search criteria returned no results"
            return updated
        else:
            raise Exception("Nothing to update")
    
    def delete(self, data):
        if data is not None:
            result = self.collection.delete_many(data)
            print("Animal Deleted")
            return result.raw_result
        else:
            raise Exception("Nothing to delete")


