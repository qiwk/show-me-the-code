# -*- coding:utf-8 -*-
import random, string

forselect = string.ascii_letters + '0123456789'

def generate(count, length):
    code = []
    for x in range(count):
        result = ""
        for y in range(length):
            result += random.choice(forselect)
        code.append(result)
    return code

code = generate(200, 20)

if __name__ == '__main__':
    print(code)

