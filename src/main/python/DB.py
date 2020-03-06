import sqlite3

conn = sqlite3.connect("MS.db")
cursor = conn.cursor()
cursor.execute("create table Jobs ( ")