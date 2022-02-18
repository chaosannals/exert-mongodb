from datetime import datetime
from pymongo import MongoClient
from cnf import settings

client = MongoClient(**settings)

rs = client.test.mdoc.find(skip=0, limit=10, sort=[('edit_time', 1)])

for r in rs:
    client.test.mdoc.update_one({
        '_id': r['_id'],
    }, {
        '$set': { 'edit_time': datetime.now(), },
    })

client.test.mdoc.update_many({
    'edit_time': { '$ne': None },
}, {
    '$set': { 'edit_m_time': datetime.now(), },
})