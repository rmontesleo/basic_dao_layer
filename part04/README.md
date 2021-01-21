# Part 4: Apply a "factorization" 


The goal of this section avoid the patter **"Repeat your self"**. In all CRUD functions (Create, Read, Update, Delete) the functions needs get the connection, create a cursor, execute the SQL statement and release the connection. 
Two functions are created execute_query and execute_commit.
- execute_query:  Get the connection, execute the sql statement, get the resultset and release the connection.
- execute_commit: Get the connection, execute the sql statement, **apply** a commit  and close the connection.

These functions leave the code cleaner, an allow the programmer focus on write the SQL statement and prepare the final result.


## Structure of the folder

1. db_functions.py : The code to connecto to database and execute sql statement. Grouped in functions
1. todo_service.py : The client or the main program who call the functions inside db_functions file.

## To run the program

```
python todo_service.py
```