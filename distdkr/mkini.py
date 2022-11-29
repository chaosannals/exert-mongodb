'''
写入初始化的配置文件
通过 mkusr.bat 创建账号
'''

import os

def make_config(cnf_template_path='conf/mongoini.yml'):
    with open(cnf_template_path,'r', encoding='utf8') as reader:
        text = reader.read()
        for i in range(1, 4):
            # 配置文件目录
            d = f'asset/s{i}/conf'
            if not os.path.isdir(d):
                os.makedirs(d)

            # 配置文件
            p = f'{d}/mongo.yml'
            with open(p, 'w', encoding='utf8') as writer:
                writer.write(text)

if __name__ == '__main__':
    make_config()