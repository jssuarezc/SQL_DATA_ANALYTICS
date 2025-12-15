import sqlite3
import pandas as pd
import os

db_name="exercise12.db"
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

queryexecute=""
df=pd.read_sql(queryexecute,conn)
print(df)
conn.close()