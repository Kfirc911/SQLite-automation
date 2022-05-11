import sqlite3
import time
from datetime import date

PATH = "C:\\Users\\Kfir Cohen\\DevOps_March_22\\DB_Git\\"
FILENAME = "Inventory.db"
FILE = PATH + FILENAME


def open_sql_connection():
    """
    This function will create connection to a database, using sqlite3 module
    This function returns a Connection object
    """
    con = sqlite3.connect(FILE)
    return con


def get_cursor(con):
    """
    This function will create a Cursor object, once a connection had been made
    :param con: sql connection
    :type con: sqlite3.connect
    :return: cursor
    :rtype: sqlite3.connect.cursor
    """
    cur = con.cursor()
    return cur


def close_sql_connection(con):
    """
    This function will commit any changes to an open sql connection and closes it.
    :param con:
    :type con: sqlite3.connect
    """
    con.commit()
    con.close()


def is_item_exist(item):
    con = open_sql_connection()  ## Creates connection
    cur = set_cursor(con)  ## Creates Cursor
    query = "SELECT * FROM `Inventory`"  ## SQL QUERY
    data = cur.execute(query).fetchall()  ## EXECUTING SQL QUERY
    close_sql_connection(con)
    for row in data:
        if row[1] == item:
            return True
    return False


is_item_exist('Tent-new')
