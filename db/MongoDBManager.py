from pymongo import MongoClient
from bson.objectid import ObjectId
from model.Curriculum import Curriculum

class MongoDBManager:
    def __init__(self, host='localhost', port=27017, username='admin', password='password', database='resume-db'):
        self.client = MongoClient(host, port, username=username, password=password)
        self.db = self.client[database]
        self.collection = self.db['curriculums']
        self.clear_collection()

    def save_curriculum(self, filename, text):
        curriculum = Curriculum(filename, text)
        result = self.collection.insert_one(curriculum.__dict__)
        return str(result.inserted_id)

    def get_curriculum(self, id):
        return self.collection.find_one({'_id': ObjectId(id)})
    
    def clear_collection(self):
        self.collection.delete_many({})
        print("Coleção 'curriculums' limpa.")
