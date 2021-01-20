#  python item01_select_all.py 

import sqlite3

connection = sqlite3.connect('../sandbox.db')
cursor = connection.cursor()

cursor.execute( ' SELECT * FROM todo ' )
result_set = cursor.fetchall()

print( result_set )

print()
print( f'The type is { type(result_set) }'  )
print( f'The size is { len(result_set ) }  ' )

last =  result_set[ -1 ]

print( f'Last element is {  last }' )
print( f'of type { type(last) }' )

cursor.close()
connection.close()