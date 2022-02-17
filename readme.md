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