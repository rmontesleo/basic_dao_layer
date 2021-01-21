# Part 7: Static methods

In the previous step we modify the methods of SQLiteDAO and put the the decorator @staticmethod. This makes a static method dont required an instance to work. Only you invoke with the name of the class and then the name of the method. 

## Structure of the folder

1. todo_dao.py : The code to connecto to database and execute sql statement. Grouped in a class TodoDAO and SQLiteDAO
1. todo_service.py : The client or the main program import the class, create an instance of TodoDAO an uses the objecto to operate.

## To run the program

```
python todo_service.py
```