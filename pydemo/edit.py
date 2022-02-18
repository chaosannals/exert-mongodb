from datetime import datetime
from pymongo import MongoClient
from cnf import settings

client = MongoClient(**settings)

rs = client.test.mdoc.find(skip=0, limit=10, sort=[('edit_time', 1)])

for r in rs:
    client.test.mdoc.update_one({
        '_id': r['_id'],
    }, {
        '$set': {'edit_time': datetime.now(), },
    })

client.test.mdoc.update_many({
    'edit_time': {'$ne': None},
}, {
    '$set': {'edit_m_time': datetime.now(), },
})

# 有更新，无插入。
rcondition = {
    'rrr': {'$eq': 123},
}
rr = client.test.mdoc.replace_one(rcondition, {
    'rrr': 123,
    'rrr_at': datetime.now(),
}, True # True 无时会插入，False 无时不插入。
)
print('r matched c:', rr.matched_count)
print('r modified c:', rr.modified_count)
print('r upserted_id: ', rr.upserted_id)
rr2 = client.test.mdoc.find_one(rcondition)
print('r :', rr2)
