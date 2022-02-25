from random import randint


WORDS = [
    'text',
    'test',
    '热结巴',
    '云计算',
    '李小福',
    '创新办',
    'easy_install',
    '好用',
    '韩玉赏鉴',
    '台中',
    '凱特琳'
]

WORDS_MAXID = len(WORDS) - 1


def rand_word():
    return WORDS[randint(0, WORDS_MAXID)]

def rand_words(length=3, extend=0):
    wc = randint(length, length + extend)
    return [WORDS[randint(0, WORDS_MAXID)] for _ in range(wc)]
