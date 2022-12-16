# Docker示例执行副本集设置

注：不是 Shared Cluster 模式。

1. 执行 mkini.py 初始化无需账号的配置
2. docker compose up -d 启动容器
3. 执行 mkusr.bat 批量创建账号（如果失败，等多一会，等服务启动完成，在没有删除 docker 挂载的数据库 data 目录情况下，可能之前已经创建好了，会提示已经存在，跳过这步。）
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


# 查询状态可以看到集群状态
rs.status()
rs.conf()

# 判断是否是分布式下的主节点
rs.isMaster()

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

分布式下，可以通过单机模式直连 directConnection=true 。由于主机是运行时选举的，所以链接的时候能直连的有可能是（示例是 27001 27002 27003） 任意一个，要试试哪个是主要的才能直连写入。

```
mongodb://root:rootpwd@localhost:27001/?authSource=admin&authMechanism=SCRAM-SHA-256&replicaSet=sn&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false
```

```
mongodb://root:rootpwd@localhost:27001/?authSource=admin&authMechanism=SCRAM-SHA-256&replicaSet=sn&readPreference=secondary&appname=MongoDB%20Compass&directConnection=true&ssl=false

mongodb://root:rootpwd@localhost:27002/?authSource=admin&authMechanism=SCRAM-SHA-256&replicaSet=sn&readPreference=secondary&appname=MongoDB%20Compass&directConnection=true&ssl=false

mongodb://root:rootpwd@localhost:27003/?authSource=admin&authMechanism=SCRAM-SHA-256&replicaSet=sn&readPreference=secondary&appname=MongoDB%20Compass&directConnection=true&ssl=false
```

## SRV

是分布式下通过域名解析，一个域名访问多个节点。