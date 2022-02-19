import os


with open('conf/mongocnf.yml','r', encoding='utf8') as reader:
    text = reader.read()
    for i in range(1, 4):
        d = f'asset/s{i}/conf'
        p = f'{d}/mongo.yml'
        if not os.path.isdir(d):
            os.makedirs(d)
        print(p)
        with open(p, 'w', encoding='utf8') as writer:
            writer.write(text)