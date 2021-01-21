import sqlite3

DB_NAME = '../sandbox.db'

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

def close_connection( conn ):
    """ The method close the connection with the database.

        Parameters
        ----------
        conn: A sqlite3 connection
        The object to close the connection with the database.
    """
    if conn is not None:
        conn.close()

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


def build_values( todo = {} ):
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


def select_all_todos():
    """ This method get all the records of the todo table. 

        Returns
        -------

        todo_list: list of dict
        The method returns a list of dictionary with the values of the records of the todo table
        Otherwise returns an empty list
    """

    conn, cursor = get_connection()
    sql = 'SELECT * FROM todo'
    cursor.execute( sql )
    todo_list = get_resultset( cursor.fetchall() )
    close_connection(conn)    
    return todo_list


def insert_todo( todo  ):
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

    conn, cursor = get_connection()
    sql = """
        INSERT INTO todo 
            (title, description, is_completed)
            VALUES( ?, ? , ? )
    """

    title, description, is_completed = build_values( todo )
    values = ( title, description, is_completed )    
    cursor.execute( sql, values )
    conn.commit()

    id = cursor.lastrowid    
    todo['id'] = id
    close_connection(conn)

    return todo


def select_by_id( id ):
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

    conn, cursor = get_connection()
    sql = 'SELECT * FROM todo WHERE id = ?'
    values = (id,)
    cursor.execute( sql, values )
    todo_list = get_resultset( cursor.fetchall() )

    close_connection(conn)

    if len( todo_list ) == 1:
        return todo_list[0]
    else:
        return {}


def delete_todo( id ):
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


    conn, cursor = get_connection()    
    sql = 'DELETE FROM todo WHERE id = ?'
    values = (id,)
    
    cursor.execute( sql, values )
    conn.commit()
    deleted_rows = cursor.rowcount
    close_connection(conn)

    return deleted_rows


def update_todo( id, todo ):
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


    conn, cursor = get_connection()
    sql = """
        UPDATE todo
        SET
            title = ?,
            description = ?,
            is_completed = ?
            WHERE id = ?    
        """

    title, description, is_completed = build_values( todo )
    values = ( title, description, is_completed, id )

    cursor.execute( sql, values )
    conn.commit()
    updated_rows = cursor.rowcount
    close_connection( conn )
    
    return updated_rows


