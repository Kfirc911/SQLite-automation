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


def data_to_item_list(cur, data):
    """
    This function is sorting data from SQL table in a dict
    This function receives cur, data, where:
    1. cur will be used to retrieve columns
    2. data will be used to retrieve values
    This function will return a list of dictionaries {columns:values}
    """
    ## List Comprehension
    columns = [description[0] for description in cur.description]  ## GETTING COLUMNS NAMES FROM DB
    result = []
    for row in data:
        item = dict(zip(columns, row))
        result.append(item)

    return result


def get_items():
    """
    This function retrieves all item information from a database
    :return: Values from DB as LIST of store items (store item is a dict)
    :rtype: list
    """
    con = open_sql_connection()  ## Creates connection
    cur = set_cursor(con)  ## Creates Cursor
    query = "SELECT * FROM Inventory"  ## SQL QUERY
    data = cur.execute(query).fetchall()  ## EXECUTING SQL QUERY
    item_list = data_to_item_list(cur, data)
    close_sql_connection(con)  ## Closing connection
    return item_list


items = get_items()
print(type(items))

for row in items:
    for key, value in row.items():
        print(f"{key}: {value}")
    print()
