import pymongo
from cnf import settings

client = pymongo.MongoClient(**settings)

manydocs = []
for i in range(1000):
    manydocs.append({
        'no': i,
        'nos': f'manydocs-{i}'
    })

client.test.mdoc.insert_many(manydocs)