import sqlite3

connection = sqlite3.connect('../sandbox.db')
cursor = connection.cursor()

id= input('Type the id you want to fetch: ')

sql = 'SELECT * FROM todo WHERE id = ? '
values = ( id, )

cursor.execute( sql, values )

result_set = cursor.fetchone()

print( f'The result is {result_set}' )

cursor.close()
connection.close()

print('Connection closed successfully')
