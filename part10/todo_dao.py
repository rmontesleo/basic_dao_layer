from sqlite_dao import SQLiteDAO

class TodoDAO(SQLiteDAO):
    """ This clas extends from SQLiteDao, that means, all the logic to connect, disconect or execute 
        sentences in the database are define in the super classes. 
        This class focus only in resolve the CRUD to the table todo of the database sandbox.
        Each method only define the requerired sql sentence and invoke the execute_query or execute_commit
        method of the parent class.
        The methods dont handle an exeption if it occours. That responsability will be of the cliente of this class. 
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
            return None


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


