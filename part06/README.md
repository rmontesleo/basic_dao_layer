# Part 6: Inheritance

In the previous step we create a class, with all functions or methods in the same class. To make more scallable our project we divide in two classes.

- SQLiteDAO: In this class we group all methods required for connect or disconnect with the database, execute query or exexute commit, or get resulset. The SQLiteDAO group all methods, could be utilized by other classes.

- TodoDAO: This class, group the specific methods to interact with the table todo. This class focus to resolve the CRUD only with the table todo.



## Structure of the folder

1. todo_dao.py : The code to connecto to database and execute sql statement. Grouped in a class TodoDAO and SQLiteDAO
1. todo_service.py : The client or the main program import the class, create an instance of TodoDAO an uses the objecto to operate.

## To run the program

```
python todo_service.py
```