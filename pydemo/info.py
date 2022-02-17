import pymongo
from cnf import settings

client = pymongo.MongoClient(**settings)

print(client.server_info())

dbs = client.list_databases()
for db in dbs:
    print(db)
