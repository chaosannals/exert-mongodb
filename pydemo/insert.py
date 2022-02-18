from random import randint
import pymongo
from cnf import settings

client = pymongo.MongoClient(**settings)

words = [
    'text',
    'test',
    '热结巴',
    '云计算',
    '李小福',
    '创新办',
    'easy_install',
    '好用',
    '韩玉赏鉴',
    '台中',
    '凱特琳'
]

wordmx = len(words) - 1

client.test.mdoc.insert_one({
    'one': 1,
    'stext': ' '.join([words[randint(0, wordmx)] for _ in range(randint(3, 6))])
})

manydocs = []
for i in range(1000):
    wc = randint(2, 5)
    ws = [words[randint(0, wordmx)] for _ in range(wc)]
    manydocs.append({
        'no': i,
        'nos': f'manydocs-{i}',
        'stext': ' '.join(ws),
    })

client.test.mdoc.insert_many(manydocs)
