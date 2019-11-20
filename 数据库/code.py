import pymysql
from pprint import pprint
 
db = pymysql.connect("localhost","root","17221070","work" )
 
cursor = db.cursor()

cursor.execute("select sname, polity, score from students;")

data = cursor.fetchall()
pprint (data)

'''Null 为群员'''
# data = list(data)
# for index, element in enumerate(data):
#     if element == 'Null':
#         data[index] = '群员   
# print(data)

db.close()
