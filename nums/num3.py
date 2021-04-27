# -*- coding:utf-8 -*-
import re

def count_word(txt):
    result = re.findall(r'[a-zA-Z-]+', txt)
    return len(result)

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        txt = f.read().lower()
        print(count_word(txt))