#!/bin/bash

# 如果用 GIT 的 Wingw 环境发现报错，换其他的，比如 Msys2 

subj='/C=CN/ST=GuangDong/L=./O=./OU=./CN=ChaosAnnals'

openssl req -newkey rsa:2048 -new -x509 -days 365 -subj $subj -nodes -out mongodb.crt -keyout mongodb.key

cat mongodb.key mongodb.crt > mongodb.pem
