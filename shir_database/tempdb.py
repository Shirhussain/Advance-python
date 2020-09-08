import  sqlite3
database = sqlite3.connect('shirdb.db')
cursor = database.cursor()

query = ''' SELECT BUYER_NAME FROM shirdb3 ORDER BY BUYER_NAME ASC'''
cursor.execute(query)

shirdb = cursor.fetchall()


for name in shirdb:
    print(name)

database.close()
