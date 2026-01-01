import os
import sqlite3
import pandas as pd

db_name="exercise24.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS stores(Store VARCHAR(10), Quarter VARCHAR(10), Amount INT)""")
# conn.commit()

# stores_data=[
#     ('S1', 'Q1', 200),
#     ('S1', 'Q2', 300),
#     ('S1', 'Q4', 400),
#     ('S2', 'Q1', 500),
#     ('S2', 'Q3', 600),
#     ('S2', 'Q4', 700),
#     ('S3', 'Q1', 800),
#     ('S3', 'Q2', 750),
#     ('S3', 'Q3', 900)
# ]
# cursor.executemany("INSERT INTO stores VALUES(?,?,?)",stores_data)
# conn.commit()

firstmethod="SELECT store, 'Q' || CAST(10-SUM(CAST(SUBSTR(quarter,-1)AS INT))AS TEXT) AS q_no FROM stores GROUP BY store"
df=pd.read_sql(firstmethod,conn)
print(df)
conn.close()