import os
# pip install pyyaml
import yaml
from random import randint

KEYFILE_CHARSER = 'qwertyuiopasdfghjklzxcvbnm0123456789'
KEYFILE_MAXID = len(KEYFILE_CHARSER) - 1

def rand_keyfile(length=1000):
    r = []
    for _ in range(1000):
        ci = randint(0, KEYFILE_MAXID)
        c = KEYFILE_CHARSER[ci]
        r.append(c)
    return ''.join(r)


def make_config(cnf_template_path='conf/mongocnf.yml'):
    key = rand_keyfile()
    with open(cnf_template_path,'r', encoding='utf8') as reader:
        cnf = yaml.load(reader, yaml.FullLoader)
        for i in range(1, 4):
            # 配置文件目录
            d = f'asset/s{i}/conf'
            if not os.path.isdir(d):
                os.makedirs(d)

            # 配置文件
            p = f'{d}/mongo.yml'
            # 同个备份集的节点，备份集名字必须一样。
            cnf['replication']['replSetName'] = f'sn'
            with open(p, 'w', encoding='utf8') as writer:
                yaml.dump(cnf, writer)

            # keyfile 由于权限必须 400 的原因，改用 dockerfile COPY 了。
            # kp = f'{d}/mongo.key'
            # with open(kp, 'w', encoding='utf8') as writer:
            #     writer.write(key)

if __name__ == '__main__':
    make_config()