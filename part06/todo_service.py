"""
In this version the class TodoDao is imported, then the object (instance) dao is created.

1) Get all todos from database and print the number of records
2) Get the todo with  id 203 (or another that exists in you db ) and print the result as dictionary
3) Create new dictionary and save the data in the database, print the result
4) Then, remove this todo from the database
5) Validate the removed todo was successfully deleted
6) Print again the data of todo with id 203
7) Update the fields of this todo in the database
8) Validate that information was updated successfully in the database

"""

from todo_dao import TodoDAO

dao = TodoDAO()

todo_list = dao.select_all_todos()
print( f'todo list size is {len(todo_list) }' )


todo_203 = dao.select_by_id(203)
print( f'Todo 203 is { todo_203 }' )

todo ={
    "title": "new chanchito todo title",
    "description": "new description",
    "is_completed": 0
}

new_todo = dao.insert_todo(todo)
print( f'THe new todo is { new_todo }' )


removed_id = new_todo['id']

deleted_rows = dao.delete_todo( removed_id  )
print( f'deleted rows? { deleted_rows }' )


deleted_todo = dao.select_by_id( removed_id )
print( f'TODO with id { removed_id } is { deleted_todo }' )


print( 'printing again todo203' )
print( todo_203 )

title = input( 'Type new title for todo 203: ' )
description = input('Type new description: ')
is_completed = input('Type 1 for completed otherwise 0: ')

updated_todo = {
    "title":title,
    "description":description,
    "is_completed":is_completed
}

updated_rows = dao.update_todo( 203, updated_todo )
print( f'updated rows { updated_rows }' )

todo_203_v2 = dao.select_by_id(203)
print( f'Validatiing changes in Todo 203 is { todo_203_v2 }' )
