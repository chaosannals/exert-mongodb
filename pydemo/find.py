from pymongo import MongoClient
from cnf import settings

client = MongoClient(**settings)

r1 = client.test.mdoc.find_one({
    'nos': {'$regex': '1', },
})

print(r1)

rs = client.test.mdoc.find(
    {
        'nos': {'$regex': '1'}
    },
    skip=10,
    limit=10,
    sort=[('nos', -1)]
)

for r in rs:
    print(r)
