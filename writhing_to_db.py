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


def insert_item(item, category, quantity, price, date):
    """
    This function inserts a new user into an existing database, once validating that Item doesnt exist
    """
    con = open_sql_connection()  ## Creates connection
    cur = set_cursor(con)  ## Creates Cursor
    if not (is_item_exist(item)):  ## is exist validation
        query = "INSERT INTO Inventory (`Item`,`Category`,`Quantity`,`Price`,`Date`) VALUES (?,?,?,?,?)"  ## PREPARED STATEMENT
        cur.execute(query, (item, category, quantity, price, date))  ## PREPARED STATEMENT
        print(f"New item had been added with values of: {item, category, quantity, price, date}")
    else:
        print("Item already exists")
    close_sql_connection(con)


insert_item(' sleeping bag', 'Outdoors', '100', '50', '03/26/22')

"""
this is for insert few things in the same time 
"""
today = date.today()
for i in range(2):
    item = input("Insert item of product: ")
    category = input("Insert name of category: ")
    quantity = input("Quantity: ")
    price = input("Price in Dollars: ")
    insert_item(item, category, quantity, price, today)
