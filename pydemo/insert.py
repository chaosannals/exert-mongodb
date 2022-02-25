import pymongo
from random import randint
from datetime import datetime
from word import rand_words
from cnf import settings

client = pymongo.MongoClient(**settings)


client.test.mdoc.insert_one({
    'one': 1,
    'stext': ' '.join(rand_words(3, 3)),
    'enter_time': datetime.now(),
})

manydocs = []
for i in range(1000):
    manydocs.append({
        'no': i,
        'nos': f'manydocs-{i}',
        'stext': ' '.join(rand_words(2, 3)),
        'skeys': rand_words(5, 3),
        'enter_time': datetime.now(),
    })

client.test.mdoc.insert_many(manydocs)
