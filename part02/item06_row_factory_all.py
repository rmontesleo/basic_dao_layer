import sqlite3

connection = sqlite3.connect('../sandbox.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute(' SELECT * FROM todo ')
result_set = cursor.fetchall()

####
print('##########################################')
print( result_set )
print()

print( f'The type is { type(result_set) }'  )
print()

print( f'The size is { len(result_set ) }  ' )
print()

last =  result_set[-1 ]
print( f'Last element is {  last }' )
print()

print( f'of type { type(last) }' )
print()
######

dict_list = [ dict( row ) for row in result_set ]

###
print('##########################################')
print( dict_list )
print()

last_json = dict_list[-1]
print( f' last json is {last_json}' )
print()

print( f' last type is { type(last_json) }' )
print()
###

connection.close()