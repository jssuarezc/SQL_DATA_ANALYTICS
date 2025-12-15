import sqlite3
import os
import pandas as pd

db_name="exercise13.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

#
cursor.execute=""
conn.commit()

string=[
    (),
    (),
    ()
]
cursor.executemany("",string)
conn.commit()
#

querytoexec=""
df=pd.read_sql(querytoexec,conn)
print(df)
conn.close()