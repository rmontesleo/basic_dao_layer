import sqlite3

DB_NAME = '../sandbox.db'


"""
In this version. We inherit form SQLIteDao

"""

class SQLiteDAO():
    def get_connection(self):
        connection = sqlite3.connect( DB_NAME )
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        return connection, cursor

    def close_connection( self, conn ):
        if conn is not None:
            conn.close()

    def get_resultset( self, fetched_data = [] ):
        result_set = [ dict( row ) for row in fetched_data ]
        return result_set


    def execute_query( self, sql , values =() ):
        conn, cursor = self.get_connection()
        cursor.execute(sql, values )
        item_list = self.get_resultset( cursor.fetchall() )
        self.close_connection(conn)
        return item_list

    def execute_commit( self, sql, values ):
        conn, cursor = self.get_connection()
        cursor.execute(sql, values)
        conn.commit()        
        rows = cursor.rowcount
        id = cursor.lastrowid
        self.close_connection(conn)
        return rows, id


class TodoDAO(SQLiteDAO):

    def build_values( self, todo = {} ):
        title = ''
        if 'title' in todo :  title = todo['title']

        description = ''
        if 'description' in todo : description = todo['description']

        is_completed = 0
        if 'is_completed' in todo: is_completed = todo['is_completed']

        return title, description, is_completed


    def select_all_todos(self):
        sql = 'SELECT * FROM todo'
        todo_list = self.execute_query(sql)
        return todo_list

    def insert_todo( self, todo  ):    
        sql = """
            INSERT INTO todo 
            (title, description, is_completed)
            VALUES( ?, ? , ? )
        """

        title, description, is_completed = self.build_values( todo )
        values = ( title, description, is_completed )    
        rows, id = self.execute_commit( sql, values )
        todo['id'] = id

        return todo


    def select_by_id( self, id ):    
        sql = 'SELECT * FROM todo WHERE id = ?'
        values = (id,)
        todo_list = self.execute_query(sql, values)

        if len( todo_list ) == 1:
            return todo_list[0]
        else:
            return {}


    def delete_todo( self, id ):    
        sql = 'DELETE FROM todo WHERE id = ?'
        values = (id,)
        deleted_rows, id = self.execute_commit( sql, values )
        return deleted_rows

    def update_todo( self, id, todo ):
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
        updated_rows, id = self.execute_commit( sql, values )
        return updated_rows