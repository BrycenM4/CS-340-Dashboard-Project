from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, pwd, host, port):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #
        # Initialize Connection
        #
        self.client = MongoClient(f"mongodb://{user}:{pwd}@{host}:{port}")
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert_one(data)  # data should be dictionary  
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, criteria=None, limit=0):
        
        if criteria is None:
            criteria = {}

        # Apply the query
        data = self.database.animals.find(criteria, {"_id": False})

        # Apply limit if specified
        if limit > 0:
            data = data.limit(limit)

        # Convert cursor to a list (important for pandas)
        return list(data)

# Create method to implement the U in CRUD.
    def update(self, initial, change):
        if initial is not None:
            if self.database.animals.count_documents(initial, limit = 1) !=0:
                update_result = self.database.animals.update_many(initial, {"$set": change})
                result = update_result.raw_result
            else: 
                result = "No document was found"
            return result
        else:
            raise Exception("Nothing to update, parameter is empty")
            
#Create method to implement the D in CRUD.
    def delete(self, remove):
        if remove is not None:
            if self.database.animals.count_documents(remove, limit = 1) != 0:
                delete_result = self.database.animals.delete_many(remove)
                result = delete_result.raw_result
            else:
                result = "No document was found"
            return result
        else:
            raise Exception("Nothing to delete, parameter is empty")