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
secondmethod="WITH CTE AS(SELECT DISTINCT store, 1 AS q_no FROM stores UNION ALL SELECT store, q_no + 1 AS q_no FROM CTE WHERE q_no <4), q AS (SELECT store, 'Q' || CAST(q_no AS CHAR(1)) AS q_no FROM CTE) SELECT q.* FROM q LEFT JOIN stores AS s ON q.store= s.store AND q.q_no = s.quarter WHERE s.store IS NULL"
thirdmethod="WITH CTE AS (SELECT DISTINCT s1.store,s2.quarter FROM stores AS s1, stores AS s2) SELECT q.* FROM CTE as q LEFT JOIN stores AS s ON q.store=s.store AND q.quarter = s.quarter WHERE s.store IS NULL"
df=pd.read_sql(thirdmethod,conn)
print(df)
conn.close()