# Part 8: Handle exceptions

Until now, if some error occurs with the database, an error with the execution of the sql statements, just stops the execution of the program.
We can handle this execptions with a block try/except.  In the block finally add code to execute ether if was successfull the try block or not.  In this case we use the block finally to close the connection with the database.

## Structure of the folder

1. todo_dao.py : The code to connecto to database and execute sql statement. Grouped in a class TodoDAO and SQLiteDAO
1. todo_service.py : The client or the main program import the class, create an instance of TodoDAO an uses the objecto to operate.

## To run the program

```
python todo_service.py
```