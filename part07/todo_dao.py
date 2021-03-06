import sqlite3

DB_NAME = '../sandbox.db'


""" In this version. Change to static methods  """

class SQLiteDAO():
    """ This class contains the methods to connect with the database """

    @staticmethod
    def get_connection():
        """ The method to obtain the connection with the database and the cursor to operate with the database.
            In the method the connection uses a row factory to obtain records instead of tupples. Then this records
            are transform in list of dictionaries.

            Returns
            -------

            connection: A sqlite3 connection object

            cursor: A sqlite3 cursor object.
        """

        connection = sqlite3.connect( DB_NAME )
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        return connection, cursor

    @staticmethod
    def close_connection( conn ):
        """ The method close the connection with the database.

            Parameters
            ----------
            conn: A sqlite3 connection
            The object to close the connection with the database.
        """

        if conn is not None:
            conn.close()

    @staticmethod
    def get_resultset( fetched_data = [] ):
        """ The method received the result of cursor.fetchall() to get a list of dictionaries.
            This method is a helper to retrieved a list of dictionaries to the client who invoke 
            the method execute_query.

            Parameters
            ----------
            fetched_data: list of fetched data.
            A list of fetched data return by teh cursor after execute a SELECT statement

            Return
            ------
            result_set: List of dictionaries
            The list of dictionaries ready to be used by the client who invoke the method execute_query.
        """

        result_set = [ dict( row ) for row in fetched_data ]
        return result_set


    @staticmethod
    def execute_query(  sql , values =() ):
        """ Execut a SQL sentence that returns the recods of some table.
            The allowed sentence is SELECT

            Parameters
            ----------

            sql: str
            The SQL sentence to execute in the database. The sentence could be only a SELECT statement.
            If the execution fails catch the exeption and throw the error.
            The connection is closed whether the execution was successful or with execption in the block finally 
            
            values:tupple
            The tupple add the parameter values to the SQL sentence to be executed.
            This is an optional parameter.

            Returns
            -------
            item_list: a list of dictionaries
            Returns a list of dictionaries that match with the executed query. 
            In case of no matched it will return an empty list            
        """

        conn, cursor = SQLiteDAO.get_connection()
        cursor.execute(sql, values )
        item_list = SQLiteDAO.get_resultset( cursor.fetchall() )
        SQLiteDAO.close_connection(conn)
        return item_list

    @staticmethod
    def execute_commit( sql, values ):
        """ Execut a SQL sentence that modifies the recods in some table.
            The allowed sentences are INSERT, UPDATE or DELETE

            Parameters
            ----------

            sql: str
            The SQL sentence to execute in the database. The sentence could be 
            an INSERT, UPDATE or DELETE. 
            If the execution fails catch the exeption and throw the error.
            The connection is closed whether the execution was successful or with execption in the block finally

            values:tupple
            The tupple add the parameter values to the SQL sentence to be executed.

            Returns
            -------
            rows: int
            The rows affected after execute the SQL statement

            id: int
            The generated id value. This apply in INSERT statement, otherwise returns None.
        """

        conn, cursor = SQLiteDAO.get_connection()
        cursor.execute(sql, values)
        conn.commit()        
        rows = cursor.rowcount
        id = cursor.lastrowid
        SQLiteDAO.close_connection(conn)
        return rows, id


class TodoDAO(SQLiteDAO):
    """ The TodoDAO is the class focus in resolve the CRUD with the 
        table todo, also could have additional methods to resolve some 
        additional solutions.
    """

    def build_values( self, todo = {} ):
        """ This method helps to insert and update todo methods to get the data in the todo dictionary.
            It helps and avoid an exeption for any key not included in the dictionary.

            Parameters
            ----------
            todo: dict
            The dictionary with the data to be updated or inserted in the table.

            Returns
            -------

            title: str
            The value of the title in the todo table

            description: str
            The value of the description in the todo table

            is_completed: int
            The value of the flag that indicate the todo is completed (1) or not (0)
        """

        title = ''
        if 'title' in todo :  title = todo['title']

        description = ''
        if 'description' in todo : description = todo['description']

        is_completed = 0
        if 'is_completed' in todo: is_completed = todo['is_completed']

        return title, description, is_completed


    def select_all_todos(self):
        """ This method get all the records of the todo table. 

            Returns
            -------

            todo_list: list of dict
            The method returns a list of dictionary with the values of the records of the todo table
            Otherwise returns an empty list
        """

        sql = 'SELECT * FROM todo'
        todo_list = super().execute_query(sql)
        return todo_list

    def insert_todo( self, todo  ):
        """ This method insert a record of the todo table. The method receive the required data in a dictionary

            Parameters
            ----------            
            todo: dict
            The dictionary with the data to be inserted in the todo table. The required fields are
            title (str), description(str) and is_completed(int with the values 1 or 0 )

            Returns
            -------

            todo: dict
            The dictionary with the generated id inside.
        """

        sql = """
            INSERT INTO todo 
            (title, description, is_completed)
            VALUES( ?, ? , ? )
        """

        title, description, is_completed = self.build_values( todo )
        values = ( title, description, is_completed )    
        rows, id = super().execute_commit( sql, values )
        todo['id'] = id

        return todo


    def select_by_id( self, id ):
        """ This method select a record of the todo table. The method receive the id of the row in the todo table.

            Parameters
            ----------
            id: int
            The id of the record in todo table to be fetch

            Returns
            -------

            todo: dict
            The required record of  todo talbe in a dictionary. If the query matches returns a dictionary with
            the required data otherwise return None.
        """

        sql = 'SELECT * FROM todo WHERE id = ?'
        values = (id,)
        todo_list = super().execute_query(sql, values)

        if len( todo_list ) == 1:
            return todo_list[0]
        else:
            return {}


    def delete_todo( self, id ):
        """ This method delete a record of the todo table. The method receive the id of the row to be deleted.

            Parameters
            ----------
            id: int
            The id of the record in todo table to be deleted

            Returns
            -------

            deleted_rows: int
            The number of deleted rows in the todo table.
        """

        sql = 'DELETE FROM todo WHERE id = ?'
        values = (id,)
        deleted_rows, id = super().execute_commit( sql, values )
        return deleted_rows

    def update_todo( self, id, todo ):
        """ This method update a record of the todo table. The method receive the id of the row and the 
            data to be modify in a dictionary.

            Parameters
            ----------
            id: int
            The id of the record in todo table to be updated

            todo: dict
            The dictionary with the data to be updated in the record.

            Returns
            -------

            updated_rows: int
            The number of updated rows in the todo table.
        """
        
        sql = """
            UPDATE todo
            SET
            title = ?,
            description = ?,
            is_completed = ?
            WHERE id = ?    
        """

        title, description, is_completed = self.build_values( todo )
        values = ( title, description, is_completed, id )
        updated_rows, id = super().execute_commit( sql, values )
        return updated_rows