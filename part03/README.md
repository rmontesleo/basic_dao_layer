# Part 3: Grouping the code using Functions


The goal of this section is separate the logic of the problem and the logic to connecto with a database and invoke only the required functions.

## Structure of the folder

1. db_functions.py : The code to connecto to database and execute sql statement. Grouped in functions
1. todo_service.py : The client or the main program who call the functions inside db_functions file.

## To run the program

```
python todo_service.py
```