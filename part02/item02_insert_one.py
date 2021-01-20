import sqlite3

connection = sqlite3.connect('../sandbox.db')
cursor = connection.cursor()

# Get the data from somewhere
title = input('Please type the title: ')
description = input('Please type the description: ')
is_completed = input( 'Is completed  0 if no, 1 for yes ' )

sql = 'INSERT INTO todo (title, description, is_completed  ) VALUES ( ?, ? , ? ) '
values = ( title, description, is_completed )

cursor.execute( sql, values )
connection.commit()

id = cursor.lastrowid

print(f'The record was added with id {id}' )


connection.close()