import sqlite3
import pandas as pd
import os

db_name="exercise10.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

#
cursor.execute("""""")
conn.commit()

string=[
    (),
    (),
    ()
]
cursor.executemany("",string)
conn.commit()
#

queryread=""
df=pd.read_sql(queryread,conn)
print(pd)
conn.close()