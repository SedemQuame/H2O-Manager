"""A simple fileto hold the various database utility functions
 and connection data to be reused ove and over again. """


#db_utils.py

import os
import sqlite3

#creating a path to connect to and create the neccesary database.

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')


def db_connect(db_path = DEFAULT_PATH):
	con = sqlite3.connect(db_path)
	return con



def create_entry(con, date_str, water_level):
	sql = """
		INSERT INTO tank (date, water_level) 
		VALUES (?, ?)"""
	cur = con.cursor()
	cur.execute(sql, (date_Str, water_level))
	return cur.lastrowid


def get_data(con):
	sql = """
		SELECT data, water_level FROM tank
	"""
	con.row_factory = sqlite3.Row
	cur = con.cursor()
	cur.execute(sql)
	#working with results ...
	result = cur.fetchone()
	date_str, water_level = result['date'], result['water_level']
	return zip(date_str, water_level)
