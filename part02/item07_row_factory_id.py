import sqlite3

connection = sqlite3.connect('../sandbox.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

##
id = input('Type the id you want to find: ')
##

cursor.execute(' SELECT * FROM todo WHERE id = ? ', (id,) )
result_set = cursor.fetchall()

dict_list = [ dict( row ) for row in result_set ]

###
print( dict_list )
size = len( dict_list )
print( f'size is { size } '  )

if size == 1 :
    print( dict_list[0]  )
else:
    print( 'no results'  )

###

connection.close()