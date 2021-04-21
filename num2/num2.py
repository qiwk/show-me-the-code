# -*- coding:utf-8 -*-
import random, string

forselect = string.ascii_letters + '0123456789'

def generate(count, length):

    for x in range(count):
        result = ''
        for y in range(length):
            result += random.choice(forselect)

        print(result)

if __name__ == '__main__':
    generate(200, 20)
