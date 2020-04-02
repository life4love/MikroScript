import sqlite3

conn = None
cursor = None
class DB_SQL(sqlite3):
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect("MikroScript.db")
        print("DB Connection established")
        self.cursor = self.conn.cursor()

    def execute(self, string):
        # string = "create table Jobs (id INT PRIMARY KEY NOT NULL, jobs_data json)"
        return cursor.execute(string)
