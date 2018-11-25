import sqlite3
from sqlite3 import Error
from config import Config 

sql_create_books_table = """ CREATE TABLE IF NOT EXISTS books (
									id integer PRIMARY KEY,
									author text NOT NULL,
									title text NOT NULL
								); """

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print("Connected to SQLite version: " + sqlite3.version)
        return conn
    except Error as e:
        print(e)
 
    return None
		
def create_table(conn, create_table_sql):
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except Error as e:
		print(e)

def main():
	conn = create_connection(Config.DATABASE_PATH)
	if conn is not None:
		# create books table
		create_table(conn, sql_create_books_table)
		conn.close()
	else:
		print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()