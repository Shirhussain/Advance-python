import sqlite3

# here i have to create a database if i have the mentioned filed it automaticaly open if i don't have so it will create ad database file 
# like here i named as 'shirdb'

try:
    database = sqlite3.connect('shirdb.db')
    database.execute(''' CREATE TABLE shirdb3(ID INT PRIMARY KEY NOT NULL, Price INT NOT NULL, Location TEXT NOT NULL, BUYER_NAME TEXT NOT NULL)''') 
    print("connected successfully")
except:
    print("connection failed")




# now i wanna use cursor 
# database cursor is a control stracture that enable traverser over the record in databse, whit that traverser we can insert recored to 
# retrieve it and remove the record as well 

database = sqlite3.connect('''shirdb.db''')
cursor = database.cursor()
cursor.execute('''INSERT INTO shirdb3(ID,PRICE,LOCATION,BUYER_NAME)VALUES(?,?,?,?) ''',(5,2500,'Outside','Trump'))
cursor.execute('''INSERT INTO shirdb3(ID,PRICE,LOCATION,BUYER_NAME)VALUES(?,?,?,?) ''',(2,444500,'Inside','shir'))
cursor.execute('''INSERT INTO shirdb3(ID,PRICE,LOCATION,BUYER_NAME)VALUES(?,?,?,?) ''',(3,99500,'Outside','Jef bezos'))
cursor.execute('''INSERT INTO shirdb3(ID,PRICE,LOCATION,BUYER_NAME)VALUES(?,?,?,?) ''',(4,50,'Outside','Mark'))
database.commit()


database.close() 



# if you wanna sor the databse 

import  sqlite3
database = sqlite3.connect('shirdb.db')
cursor = database.cursor()

query = ''' SELECT BUYER_NAME FROM shirdb3 ORDER BY BUYER_NAME ASC'''
cursor.execute(query)

shirdb = cursor.fetchall()


for name in shirdb:
    print(name)

database.close()


import  sqlite3
database = sqlite3.connect('shirdb.db')
cursor = database.cursor()

query = ''' SELECT BUYER_NAME FROM shirdb3  LIMIT 3 OFFSET 4'''
cursor.execute(query)

shirdb = cursor.fetchall()


for name in shirdb:
    print(name)

database.close()

import  sqlite3
database = sqlite3.connect('shirdb.db')
cursor = database.cursor()


# select the id in mentioned here
#query = ''' SELECT BUYER_NAME FROM shirdb3 WHERE ID IN(3,5,1)'''
#query = ''' SELECT BUYER_NAME FROM shirdb3 WHERE PRICE>100'''
#query = ''' SELECT BUYER_NAME FROM shirdb3 WHERE ID NOT IN(3,1)'''
# show only ends with 'r', or 'os'
#query = ''' SELECT BUYER_NAME FROM shirdb3 WHERE BUYER_NAME LIKE '%r' '''
#query = ''' SELECT BUYER_NAME FROM shirdb3 WHERE BUYER_NAME LIKE '%os' '''
# show the record if you see  's' in table anywhere you see 's'
query = ''' SELECT BUYER_NAME FROM shirdb3 WHERE BUYER_NAME LIKE '%s%' '''
cursor.execute(query)

shirdb = cursor.fetchall()


for name in shirdb:
    print(name)

database.close()








import  sqlite3
database = sqlite3.connect('shirdb.db')
cursor = database.cursor()

#delete a row in database
query = ''' DELETE FROM shirdb3 WHERE BUYER_NAME LIKE '%tr$' '''
cursor.execute(query)

shirdb = cursor.fetchall()

for name in shirdb:
    print(name)

database.close()




import sqlite3

db = sqlite3.connect('shirdb.db')
cursor = db.cursor()



# if you have dublicate row or dublicate row data, so you wanna have only one of them 
query = 'SELECT DISTINCT BUYER_NAME FROM shirdb3'
cursor.execute(query)

name_of_people = cursor.fetchall()


for name in name_of_people:
    print(name)


db.commit()
db.close()




import sqlite3

db = sqlite3.connect('shirdb.db')

cursor = db.cursor()

#block operator 
#block operator is very kind of semllar to 'like' operator but unlike to block operator is case sensetive and block operator is case sensetive 

# star '*'  it meanse that all but question mark '?' match only one carrector

#query = ''' SELECT BUYER_NAME FROM shirdb3 WHERE BUYER_NAME GLOB 's*' '''
#it means that after 'rk' any number of carrector can be but befor only one currector is allowed
#query = ''' SELECT BUYER_NAME FROM shirdb3 WHERE BUYER_NAME GLOB '?ir*' '''
#print the name which has number inside 
#query = ''' SELECT BUYER_NAME FROM shirdb3 WHERE BUYER_NAME GLOB '*[1-9]*' '''
# it means that give me the name which start with A,B,C,D
query = ''' SELECT BUYER_NAME FROM shirdb3 WHERE BUYER_NAME GLOB '[A-D]*' '''
cursor.execute(query)

names = cursor.fetchall()

for name in names:
    print(name)





import sqlite3

db = sqlite3.connect('student_records.db')
cursor = db.cursor()

#IF YOU  wanna find the union between two table like to 'set' so you can do as follows
#query = ''' SELECT dept_name FROM 'std table' UNION SELECT dept_name FROM teacher_table'''
#intersect two table is like intersecting two set 
query = ''' SELECT dept_name FROM 'std table' INTERSECT SELECT dept_name FROM teacher_table'''
cursor.execute(query)

records= cursor.fetchall()

for record in records:
    print(record)

db.commit()
db.close()



import sqlite3

db = sqlite3.connect('shirdb.db')
cursor = db.cursor()


#math in sqlite3

#query = '''SELECT random()'''
#select rounded value with '2' dicmal places
query = ''' SELECT round(98.939434,2)'''
cursor.execute(query)


random_number = cursor.fetchall()

for random in random_number:
    print(random)

# it will give us random value between '+- 922337203685477808'





import sqlite3

db = sqlite3.connect('student_records.db')

cursor = db.cursor()
#agregation in sqlite3
# query = '''SELECT AVG(marks) '''
#query = ''' SELECT AVG(marks) FROM students WHERE ID<8'''

# if you wanna distinct the mark wich has the same value
#query = '''SELECT AVG(DISTINCT mark) FROM students '''

# if you wanna count 
#query = '''SELECT COUNT(*) FROM students'''


#if you wanna find the uniqe one 
#query = '''SELECT COUNT(DISTINCT marks) FROM students'''
#query = '''SELECT COUNT(DISTINCT marks) FROM students WHERE LIKE "s%" '''

#find the maximum/minmum 'id'
#query = '''SELECT MAX(ID) FROM studnets'''
#query = '''SELECT SUM(ID) FROM students'''


#find absolute value --> if we have any nigative vlaue with absolute we can convert to positive integer filed 
#query = '''SELECT ABS(marks) FROM students'''
cursor.execute(query)

marks = cursor.fetchall()
for mark in marks:
    print(mark)



import sqlite3

db = sqlite3.connect('shirdb.db')

cursor = db.cursor()


#string --> substring --- here i wanna print the string that word wich start from two it means that starting from 'h' 
#query = '''SELECT substr('Shir',2)'''

#next time i wanna start from '2' and just print '5' character
#query = '''SELECT substr('jef bezos',2,5)'''
#query = '''SELECT substr('jef bezos',-1,5)'''


#if you wanna remove some character from the start and end of character, you should use 'Trim'

#query = '''SELECT Trim('rshir','r')'''


# if you wannasome spaces 
#query = '''SELECT Trim(' shir') '''

#if you wanna remove from left of word 'LTrim', but right is 'Rtrim'
#query = ''' SELECT LTrim('####shir###','#')'''

#making upercase or lowercase 
#query = '''SELECT Upper('shir')'''

query = '''SELECT Lower('SHIR')'''
records = cursor.execute(query)

for record in records:
    print(record)

db.commit()
db.close()











