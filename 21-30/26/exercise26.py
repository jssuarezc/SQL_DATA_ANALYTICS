import os
import sqlite3
import pandas as pd

db_name="exercise26.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS covid(city VARCHAR(50), days DATE, cases INT)""")
conn.commit()

cursor.execute("DELETE FROM covid")
conn.commit()

delhi_vals=[
    ('DELHI','2022-01-01',100),
    ('DELHI','2022-01-02',200),
    ('DELHI','2022-01-03',300)
]
cursor.executemany("INSERT INTO covid VALUES(?,?,?)",delhi_vals)
conn.commit()

mumbai_vals=[
    ('MUMBAI','2022-01-01',100),
    ('MUMBAI','2022-01-02',100),
    ('MUMBAI','2022-01-03',300)
]
cursor.executemany("INSERT INTO covid VALUES(?,?,?)",mumbai_vals)
conn.commit()

chennai_vals=[
    ('CHENNAI','2022-01-01',100),
    ('CHENNAI','2022-01-02',200),
    ('CHENNAI','2022-01-03',150)
]
cursor.executemany("INSERT INTO covid VALUES(?,?,?)",chennai_vals)
conn.commit()

bangalore_vals=[
    ('BANGALORE','2022-01-01',100),
    ('BANGALORE','2022-01-02',300),
    ('BANGALORE','2022-01-03',200),
    ('BANGALORE','2022-01-04',400)
]
cursor.executemany("INSERT INTO covid VALUES(?,?,?)",bangalore_vals)
conn.commit()

querytoexec="WITH xxx AS (SELECT *, RANK() OVER(PARTITION BY city ORDER BY days ASC) as rn_days, RANK() OVER (PARTITION BY city ORDER BY cases ASC) AS rn_cases, RANK() OVER (PARTITION BY city ORDER BY days ASC) - RANK() OVER(PARTITION BY city ORDER BY cases ASC) AS diff FROM covid) SELECT city FROM xxx GROUP BY city HAVING COUNT(DISTINCT diff) = 1 AND AVG(diff)=0"
df=pd.read_sql(querytoexec,conn)
print(df)
conn.close()