# Part 10: Split the classes in different files.

---

In this section shows how to separate the classes in different files.

- **base_dao.py** : Contains the AbstracDAO class. This class define the required methods (like an interface)
- **sqlite_dao.py**: Contains the SQLiteDAO class that extends from AbstractDAO. This class implements the required methods to connect, disconnect or execute sentences in the database.
- **todo_dao.py**: Contains TodoDAO class that extends from SQLiteDAO and it focus on work with the CRUD.
- **todo_service.py**: This is the script that execute the main program. It imports the TodoDAO, and only invoke the define methods in this class to fetch or modify records in the database.

---

## To work with this sample, its required

1. Start or Activate the virtual environment from the root folder.
```
pipenv shell
```

2. Verify the database and the table todo ared created.

3. Create an .env file  with the variable DATABASE and where is is located the database. The .env file must be created inside this folder. In this sample the content of the .env file is
```
DATABASE=../sandbox.db
```

4. Verify the shell is inside the part10 folder. Type the following command and press enter at the end.
```
python todo_service.py
```
---


## The structure of this folder

1. .env  file
1. sqlite_dao.py
1. todo_dao.py
1. todo_service.py





