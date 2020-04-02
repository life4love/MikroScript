import sqlite3
import json
from datetime import datetime


conn = sqlite3.connect("MikroScript.db")
cursor = conn.execute(''' SELECT * FROM jobs  ''')
for rec in cursor:
    print(rec)
cursor.close()
conn.close()

