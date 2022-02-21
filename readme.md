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

## Docker示例执行副本集设置

1. 执行 mkini.py 初始化无需账号的配置
2. docker compose up -d 启动容器
3. 执行 mkusr.bat 批量创建账号（如果失败，等多一会，等服务启动完成）
4. 执行 mkcnf.py 重置配置为需要账号且集群化的配置
5. docker compose restart 重启容器
6. 执行 mkrep.bat 配置集群各个节点路由（如果失败，等多一会，配置分布式后节点重启会比较久。）

注：如果重试，要删掉数据库的所有数据文件。

### 大概流程

注： keyFile 的文件权限必须 400 ，所属用户必须是 mongod 进程的用户。

```bash
db.auth({
  user: 'root',
  pwd: 'rootpwd',
  mechanism: 'SCRAM-SHA-256'
})

use admin
db.createUser({
  user: 'root',
  pwd: 'rootpwd',
  roles: ['root']
})
db.createUser({
  user: 'root',
  pwd: 'rootpwd',
  roles: [{ role: 'userAdminAnyDatabase', db:'admin'}]
})


# 查询状态
rs.status()
rs.conf()

# 一次配置
rs.initiate({
  _id:"sn", members:[
    { _id:0,host: "exert-mongodb-server-1:27017" },
    { _id:1,host: "exert-mongodb-server-2:27017" },
    { _id:2,host: "exert-mongodb-server-3:27017" }
  ]
})
# 或者
rs.initiate()
rs.add("exert-mongodb-server-1:27017")
rs.add("exert-mongodb-server-2:27017")
rs.add("exert-mongodb-server-3:27017")
```

注：使用多个地址链接时，需要开启 TLS 加密

## Mongo Compress

分布式下，可以通过单机模式直连 directConnection=true 。

```
mongodb://root:rootpwd@localhost:27001/?authSource=admin&authMechanism=SCRAM-SHA-256&replicaSet=sn&readPreference=secondary&appname=MongoDB%20Compass&directConnection=true&ssl=false

mongodb://root:rootpwd@localhost:27002/?authSource=admin&authMechanism=SCRAM-SHA-256&replicaSet=sn&readPreference=secondary&appname=MongoDB%20Compass&directConnection=true&ssl=false

mongodb://root:rootpwd@localhost:27003/?authSource=admin&authMechanism=SCRAM-SHA-256&replicaSet=sn&readPreference=secondary&appname=MongoDB%20Compass&directConnection=true&ssl=false
```

## SRV

是分布式下通过域名解析，一个域名访问多个节点。