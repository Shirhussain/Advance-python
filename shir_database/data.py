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

