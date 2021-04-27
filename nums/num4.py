# -*- coding:utf-8 -*-
"""
作者：Administrator
日期：2021年04月26日
"""
import pymysql
#import sys
#sys.path.append(r"E:\PycharmProjects\git-projects\show-me-the-code\num2")
from num2 import num2

mydb = pymysql.connect(host="localhost", user="root", password="970916")
mycursor = mydb.cursor()
#mycursor.execute('CREATE DATABASE showcode')
mycursor.execute("USE showcode")
mycursor.execute('DROP TABLE IF EXISTS atvcode')
mycursor.execute('CREATE TABLE atvcode(id INT  NOT NULL AUTO_INCREMENT PRIMARY KEY, code char(50) NOT NULL)')
# sql = "INSERT INTO atvcode(id, code) VALUES (%s, '%s')" % (1, '125kMac')
# mycursor.execute(sql)

mycode = num2.code
for i in range(len(mycode)):
    #s = mycode[i]
    mycursor.execute("INSERT INTO atvcode(code) VALUES('%s')" % mycode[i])
mydb.commit()
mydb.close()

if __name__ == "__main__":
    print(mycode)
