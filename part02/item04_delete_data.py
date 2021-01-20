import sqlite3

connection = sqlite3.connect('../sandbox.db')
cursor = connection.cursor()

id = input('Type the id of todo to delete: ')

sql = 'DELETE FROM todo WHERE id = ?'
values = ( id, )
cursor.execute( sql, values )
connection.commit()
deleted_rows = cursor.rowcount
connection.close()


print( f' Total deleted was {deleted_rows} ')
print('Connection successfully closed')