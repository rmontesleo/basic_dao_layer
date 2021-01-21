# Part 9: Abstract Class

The interfaces helpus to implements design patterns. In this sample and abstract class was selected to define abstract methods.
This abstract methods define the contract(the interface) and other class will have the responsability to implement those methods.
In this way we decouple the python code with the selected database. The data layer will have 3 steps.

- AbstractDAO: Define the methods to implements.
- SQLiteDAO: Implements the methods and define how to connect with the database.
- TodoDAO: This class is responsible to implement the CRUD.


## Structure of the folder

1. todo_dao.py : The code to connecto to database and execute sql statement. Grouped in the classes AbastractDAO, TodoDAO and SQLiteDAO
1. todo_service.py : The client or the main program import the class, create an instance of TodoDAO an uses the objecto to operate.

## To run the program

```
python todo_service.py
```