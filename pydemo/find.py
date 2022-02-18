from pymongo import MongoClient
from cnf import settings

client = MongoClient(**settings)

r1 = client.test.mdoc.find_one({
    'nos': {'$regex': '1', },
})

if r1 is None:
    print('r1 is None')

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

print('==============================')

rts = client.test.mdoc.find(
    {
        '$text': { '$search': 'text 台中' },
    },
    projection={
        'score': { '$meta': 'textScore', },
    },
    skip=10,
    limit=10,
    sort=[('score', { '$meta': 'textScore' })]
)

for rt in rts:
    print(rt)
