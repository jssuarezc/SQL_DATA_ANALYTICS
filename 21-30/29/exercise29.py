import os
import sqlite3
import pandas as pd

db_name="exercise29.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS subscriber(sms_date DATE, sender VARCHAR(20), receiver VARCHAR(20), sms_no INT)""")
# conn.commit()

# sub_vals=[
#     ('2020-4-1', 'Avinash', 'Vibhor',10),
#     ('2020-4-1', 'Vibhor', 'Avinash',20),
#     ('2020-4-1', 'Avinash', 'Pawan',30),
#     ('2020-4-1', 'Pawan', 'Avinash',20),
#     ('2020-4-1', 'Vibhor', 'Pawan',5),
#     ('2020-4-1', 'Pawan', 'Vibhor',8),
#     ('2020-4-1', 'Vibhor', 'Deepak',50)
# ]
# cursor.executemany("INSERT INTO subscriber VALUES(?,?,?,?)",sub_vals)
# conn.commit()

queryA="SELECT * FROM subscriber"
df=pd.read_sql(queryA,conn)
print(df)
queryB="SELECT sms_date, p1, p2, SUM(sms_no) AS total_sms FROM(SELECT sms_date, CASE WHEN sender < receiver THEN sender ELSE receiver END AS p1, CASE WHEN sender > receiver THEN sender ELSE receiver END AS p2, sms_no FROM subscriber) AS A GROUP BY sms_date,p1,p2"
df1=pd.read_sql(queryB,conn)
print(df1)
conn.close()