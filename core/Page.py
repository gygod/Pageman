import pymongo
from config import getData

db_data = getData()

connection = pymongo.MongoClient(db_data['host'],db_data['port'])

db = connection['pageman']
db.authenticate(db_data['username'],db_data['password'])

result = db.users.find({})

for doc in result:
    print(doc)
