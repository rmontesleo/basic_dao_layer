# Part 5: Using classes 

After refactoring the code and avoid duplications, all functions are group in a class. This class is an abstraction that represents an entity of the system.  In this step all previous functions were added in the samae class.


## Structure of the folder

1. todo_dao.py : The code to connecto to database and execute sql statement. Grouped in a class TodoDAO
1. todo_service.py : The client or the main program import the class, create an instance of TodoDAO an uses the objecto to operate.

## To run the program

```
python todo_service.py
```