docker exec -it exert-mongodb-server-1 mongo --eval "db.createUser({ user: 'root', pwd: 'rootpwd', roles: ['root'] })" 127.0.0.1:27017/admin
docker exec -it exert-mongodb-server-2 mongo --eval "db.createUser({ user: 'root', pwd: 'rootpwd', roles: ['root'] })" 127.0.0.1:27017/admin
docker exec -it exert-mongodb-server-3 mongo --eval "db.createUser({ user: 'root', pwd: 'rootpwd', roles: ['root'] })" 127.0.0.1:27017/admin
