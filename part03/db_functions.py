import sqlite3

DB_NAME = '../sandbox.db'

def get_connection():
    connection = sqlite3.connect( DB_NAME )
    
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    return connection, cursor

def close_connection( conn ):
    if conn is not None:
        conn.close()

def get_resultset( fetched_data = [] ):
    result_set = [ dict( row ) for row in fetched_data ]
    return result_set


def build_values( todo = {} ):
    title = ''
    if 'title' in todo :  title = todo['title']

    description = ''
    if 'description' in todo : description = todo['description']

    is_completed = 0
    if 'is_completed' in todo: is_completed = todo['is_completed']

    return title, description, is_completed


def select_all_todos():
    conn, cursor = get_connection()
    sql = 'SELECT * FROM todo'
    cursor.execute( sql )
    todo_list = get_resultset( cursor.fetchall() )
    close_connection(conn)    
    return todo_list


def insert_todo( todo  ):
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
    conn, cursor = get_connection()    
    sql = 'DELETE FROM todo WHERE id = ?'
    values = (id,)
    
    cursor.execute( sql, values )
    conn.commit()
    deleted_rows = cursor.rowcount
    close_connection(conn)

    return deleted_rows


def update_todo( id, todo ):
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


