# Shard Cluster

TODO

```js
// router 服务器的 admin 库 通过 addShard 加入分片
db.runCommand({'addShard':'s1/127.0.0.1:27141,127.0.0.1:27142,127.0.0.1:27143'});
db.runCommand({'addShard':'s2/127.0.0.1:27241,127.0.0.1:27242,127.0.0.1:27243'});

// 开启分片 exert 是 schema
db.runCommand({ enablesharding: 'exert' });

// 配置可分片集合

// 索引
db.users.ensureIndex({'alias':'hashed'});
// 
db.runCommand({ shardcollection: 'exert.users', key: { 'alias': 'hashed' }});
```
