from db_utils import db_connect 

con = db_connect()	#connect to the database.
cur = con_cursor()	#instantiate a cursor obj.

tank_sql = """
CREATE TABLE IF NOT EXISTS tank (
	date text PRIMARY KEY,
	water_level text NOT NULL
)"""

cur.execute(tank_sql)


