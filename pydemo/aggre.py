import pymongo
from cnf import settings


client = pymongo.MongoClient(**settings)

# 管道逐步进行数据处理。
rs1 = client.test.mdoc.aggregate([
    {
        '$match': {'skeys': '云计算'}
    },
    {
        '$group': {
            # 用到字段的时候要用 $ 开头。
            # '_id': ['$no', '$nos'],
            # '_id': '$no',
            '_id': { 'no': '$no', 'no2': '$nos' },
            'count': { '$sum': 1 },
            'stext': { '$first': '$stext' },
            'skeys': { '$last': '$skeys' },
        },
    },
    {
        '$sort': { 'count': -1 },
    },
    {
        '$skip': 10,
    },
    {
        '$limit': 10
    }
])

for r in rs1:
    print(r)

print('----------------------------------------')
rs2 = client.test.mdoc.aggregate([
    {
        # 字段名加 $ 前缀
        '$unwind': '$skeys',
    },
    {
        '$skip': 10,
    },
    {
        '$limit': 10
    },
])

for r in rs2:
    print(r)

print('----------------------------------------')
rs3 = client.test.mdoc.aggregate([
    {
        # 字段名加 $ 前缀
        '$lookup': {
            'localField': 'no', # mdoc.no
            'from': 'tdoc',
            'foreignField': 'tid',
            'as': 'tdata',
        },
    },
    {
        '$limit': 10
    },
])

for r in rs3:
    print(r)