import os
import sqlite3
import pandas as pd

db_name="exercise20.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS UserActivity(username VARCHAR(20),activity VARCHAR(20), startDate DATE, endDate DATE)""")
# conn.commit()

# UserActivity_data=[
#     ('Alice','Travel','2020-02-12','2020-02-20'),
#     ('Alice','Dancing','2020-02-21','2020-02-23'),
#     ('Alice','Travel','2020-02-24','2020-02-28'),
#     ('Bob','Travel','2020-02-11','2020-02-18')
# ]

# cursor.executemany("INSERT INTO UserActivity VALUES(?,?,?,?)",UserActivity_data)
# conn.commit()

querytoexec="WITH CTE AS (SELECT * , COUNT(1) OVER (PARTITION BY username) AS total_activities, RANK() OVER(PARTITION BY username ORDER BY startdate DESC) AS rnk FROM UserActivity) SELECT * FROM CTE WHERE total_activities=1 OR rnk=2"
df=pd.read_sql(querytoexec,conn)
print(df)
conn.close()