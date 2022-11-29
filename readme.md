# exert-mongodb

mongosh 命令行创建用户。

```mongosh
// 切换数据库到 admin 这个下的角色权限高，root 仅在这个库有
use admin


db.createUser({
    user: 'root',
    pwd: 'password123',
    roles: ['root']
    // roles: [{ role:'root', db: 'admin' }]
})
```


## 必须配置强制权限

添加账号后再设置，不然会登录不了。


### mongo 4.* 或 5.*

把默认 authorization: disabled 改成 enabled 强制要求账号登录。

net: bindIp: 127.0.0.1 改成 0.0.0.0 支持外网访问。

```yaml
security:
  authorization: enabled
  javascriptEnabled: false

net:
  port: 27017
  bindIp: 0.0.0.0
```

### mongosh 授权

```bash
db.auth({
  user: 'root',
  pwd: 'root',
  mechanism: 'SCRAM-SHA-256'
})
```

## 事务

注：mongo 的事务是分布式事务，基于集群，所以必须以集群才能使用。配置为单节点模式无法使用。

配置文件 给 本地节点 mongo 服务器 指定个名字。
```yaml
replication:
  replSetName: rs0
```

进入命令行模式
```bash
mongo
```

命令行下配置集群，指定 集群节点（只有1个），并指定该节点为主节点。
```mongosh
rs.initiate({_id:"rs0", members:[{_id:0,host: "127.0.0.1:27017",priority:1}]})
```
