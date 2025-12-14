import sqlite3
import pandas as pd
import os

db_name="exercise04.db"
conn = sqlite3.connect(db_name)
cursor= conn.cursor()

###
cursor.execute("""""")
conn.commit()

string=[
    (),
    (),
    ()
]
cursor.executemany("",string)
conn.commit()

######
querytoexecute=""
df=pd.read_sql(querytoexecute,conn)
print(df)
conn.close()
