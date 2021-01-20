import sqlite3

connection = sqlite3.connect('../sandbox.db')
cursor = connection.cursor()

id = input('Type the id of the todo: ')
title = input('Type the new title: ')
description = input('Type the new description : ')
is_completed = input('is completed? (0/1): ')

sql = """
UPDATE todo
SET
    title = ?,
    description = ?,
    is_completed = ?
WHERE id = ?    
"""
values = ( title, description, is_completed, id )

cursor.execute( sql, values )
connection.commit()
updated_rows =  cursor.rowcount
connection.close()

print( f'Total of updated rows {updated_rows}' )
print('Connection closed')