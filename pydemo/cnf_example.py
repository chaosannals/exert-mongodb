# 配置详见 pymongo 源码 mongo_client.py MongoClient 初始化参数注释。
settings = {
    'host':'127.0.0.1',
    'port':27017,
    'directConnection': True, # 强制单机链接，此时即使是集群也没有启动读写分离。
    # 'username': 'root',
    # 'password': '',
    # 'authMechanism': 'SCRAM-SHA-256'
    # 'replicaSet': 'sn'
}