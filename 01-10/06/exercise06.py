import sqlite3
import os
import pandas as pd

db_name="exercise06.db"
conn=sqlite3.cursor(db_name)
cursor=conn.cursor()

###
cursor.execute("""""")
conn.commit()

string = [
    (),
    (),
    ()
]
cursor.executemany("",string)
conn.commit()
###

queryexecute=""
df=pd.read_sql(queryexecute,conn)
print(df)
conn.close()