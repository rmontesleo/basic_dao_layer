"""
    In this version we put each class in a different file
"""

from abc import ABC, abstractmethod



class AbstractDAO(ABC):
    """
        This abstract class is used like template or interface to define methods.
        The implementation of the abstract methods depends on the required database.
        Only the close_connection method is define in this class.  The rest of methods
        are only declared, but not implemented
    """

    @staticmethod
    @abstractmethod
    def get_connection():
        """
            The implementation of this method depends on the used database
        """
        raise NotImplemented


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
    @abstractmethod
    def execute_query(  sql , values =() ):
        """
            The implementation of this method depends on the used database
        """
        raise NotImplemented

    @staticmethod
    @abstractmethod
    def execute_commit( sql, values ):
        """
            The implementation of this method depends on the used database
        """
        raise NotImplemented