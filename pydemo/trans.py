from random import randint
from datetime import datetime
from time import time_ns
from pymongo import MongoClient, ReadPreference
from pymongo.read_concern import ReadConcern
from pymongo.write_concern import WriteConcern
from cnf import settings

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


client = MongoClient(
    retryWrites=False, # 事务需要关闭重试写入
    **settings
)

with client.start_session() as session:
    with session.start_transaction(
        read_concern=ReadConcern('snapshot'),
        write_concern=WriteConcern('majority'),
        read_preference=ReadPreference.PRIMARY
    ):
        rows = []
        gid = time_ns()
        for i in range(100):
            wc = randint(2, 5)
            ws = [words[randint(0, wordmx)] for _ in range(wc)]
            rows.append({
                'tid': i,
                'gid': gid,
                'tn': f'manytdocs-{i}',
                'stext': ' '.join(ws),
                'enter_at': datetime.now()
            })
        client.test.tdoc.insert_many(rows, session=session)
        
        # 不能中途提交，会导致事务关闭。
        # session.commit_transaction()

        rows = []
        gid = time_ns()
        for i in range(100, 200):
            wc = randint(2, 5)
            ws = [words[randint(0, wordmx)] for _ in range(wc)]
            rows.append({
                'tid': i,
                'gid': gid,
                'tn': f'manytdocs-{i}',
                'stext': ' '.join(ws),
                'enter_at': datetime.now()
            })
        client.test.tdoc.insert_many(rows, session=session)
        session.commit_transaction()
    