# Install the Database


## Install SQLite3 on ubuntu.

1. Execute the command

```
sudo apt-get install sqlite3 libsqlite3-dev
```

2. Verify the installation with

```
sqlite3 --version
```

3. In the root folder use the command to create the database with the script item01_ddl_scripts.sql contained in the folder part01
```
cat part01/item01_ddl_scripts.sql | sqlite3 sandbox.db
```

4. Check the instalation of the database. Connect with sqlite
```
sqlite3 sandbox.db
```

5. The prompt change to sqlite> .  In that prompt type .schema to see all tables and the dll or .table to see the name of the created tables. It's important use the dot before the word schema

```
sqlite> .schema
```

6. It's important use the dot before the word table
```
sqlite> .table
```

7. Check the number of records. In this point the table contains zero records. ***REMEMBER USE ; AT THE END OF SQL STATEMENTS**
```
SELECT * FROM todo;
```


8. To quit type .quit an enter. It's important use the dot before the word quit
```
sqlite> .quit
```

9. Create an initial data run the script item02_data_scripts.sql in the folder part01 to insert data in the table. The following command run in terminal
```
cat part01/item02_data_scripts.sql  | sqlite3 sandbox.db
```

10. Connect again to sqlite and check 
```
sqlite3 sandbox.db
```

11. Check the number of records. This time 208 records where added to the table
```
SELECT * FROM todo;
```

```
SELECT COUNT(*) FROM todo;
```

12. Quit from sqlite shell
```
sqlite> .quit
```



