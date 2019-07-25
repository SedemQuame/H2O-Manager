"""A simple fileto hold the various database utility functions
 and connection data to be reused ove and over again. """
import os
import sqlite3

#creating a path to connect to and create the neccesary database.
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')


def db_connect(db_path = DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con


def create_table(con):
    sql = """
        CREATE TABLE IF NOT EXISTS tank(
            data text NOT NULL,
            water_level text NOT NULL
        )
        """
    cur = con.cursor()
    cur.execute(sql)
    con.commit()


def create_entry(con, date_str, water_level):
    create_table(db_connect())
    sql = """
        INSERT INTO tank (data, water_level) 
        VALUES (?, ?)"""
    cur = con.cursor()
    cur.execute(sql, (date_str, water_level))
    con.commit()
    return cur.lastrowid

    print(create_entry(db_connect(), "2019-11-04", "65"))
 
def get_data(con):
    create_table(db_connect())
    sql = """
        SELECT * FROM tank
    """
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    return cur.fetchall()

get_data(db_connect())
