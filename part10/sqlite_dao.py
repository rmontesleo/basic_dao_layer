import os
import sqlite3
from dotenv import load_dotenv

from base_dao import AbstractDAO

load_dotenv()

DB_NAME = os.environ.get('DATABASE')


class SQLiteDAO(AbstractDAO):
    """
        This class extends of AbstractDAO and must implements the inherited and abstract methods, to be usefull for some client.
        This clas implements the methods considering , they will be implemented to work with SQLite3.

        The parameter of the database is passed by environment variable. This need and .env file to get the value of the 
        DATABASE indicating how to get to the database.
    """

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
    def get_resultset( fetched_data = [] ):
        """The method received the result of cursor.fetchall() to get a list of dictionaries.
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
        """Execut a SQL sentence that returns the recods of some table.
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

        try:
            conn, cursor = SQLiteDAO.get_connection()
            cursor.execute(sql, values )
            item_list = SQLiteDAO.get_resultset( cursor.fetchall() )
            return item_list
        except sqlite3.Error as error:
            print( f'Query error is {error}' )
            raise error
        finally:
            """
            Finally we invoke the close_connection method in the finally block
            If you required add something else, implement your required logic
            """
            SQLiteDAO.close_connection(conn)


    @staticmethod
    def execute_commit( sql, values ):
        """Execut a SQL sentence that modifies the recods in some table.
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
        
        try:
            conn, cursor = SQLiteDAO.get_connection()
            cursor.execute(sql, values)
            conn.commit()        
            rows = cursor.rowcount
            id = cursor.lastrowid
            SQLiteDAO.close_connection(conn)
            return rows, id
        except sqlite3.Error as error:
            print( f'Commit error is {error}')
            raise error
        finally:
            """
            Finally we invoke the close_connection method in the finally block
            If you required add something else, implement your required logic
            """
            SQLiteDAO.close_connection(conn)     
