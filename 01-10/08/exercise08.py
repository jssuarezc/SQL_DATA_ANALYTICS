import sqlite3
import os
import pandas as pd

db_name="exercise08.db"
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

queryexec=""
df=pd.read_sql(queryexec,conn)
conn.close()
