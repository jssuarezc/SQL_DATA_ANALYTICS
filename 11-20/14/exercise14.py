import sqlite3
import pandas as pd
import os

db_name="exercise14.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS spending(user_id INT, spend_date DATE, platform VARCHAR(50), amount INT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS all_spend(spend_date DATE, platform VARCHAR(50), total_amount INT, total_users INT)""")
conn.commit()

spending_data=[
    (1,'2019-07-01','mobile',100),
    (1,'2019-07-01','desktop',100),
    (2,'2019-07-01','mobile',100),
    (2,'2019-07-02','mobile',100),
    (3,'2019-07-01','desktop',100),
    (3,'2019-07-02','desktop',100)
]
cursor.executemany("INSERT INTO spending VALUES(?,?,?,?)",spending_data)

all_spend_data=[
    ('2019-07-01','mobile',100,1),
    ('2019-07-01','desktop',100,1),
    ('2019-07-01','both',200,1),
    ('2019-07-02','mobile',100,1),
    ('2019-07-02','desktop',100,1),
    ('2019-07-02','both',0,0),
]
cursor.executemany("INSERT INTO all_spend VALUES(?,?,?,?)",all_spend_data)
conn.commit

querytoexecute="WITH all_spend AS (SELECT spend_date, user_id, MAX(platform) AS platform, SUM(amount) AS amount FROM spending GROUP BY spend_date, user_id HAVING COUNT(DISTINCT platform)=1 UNION ALL SELECT spend_date, user_id, 'both' AS platform, SUM(amount) AS amount FROM spending GROUP BY spend_date, user_id HAVING COUNT(DISTINCT platform)=2 UNION ALL SELECT DISTINCT spend_date, null AS user_id, 'both' AS platform, 0 AS amount FROM spending) SELECT spend_date, platform, SUM(amount) AS total_amount, COUNT(DISTINCT user_id) AS total_users FROM all_spend GROUP BY spend_date, platform ORDER BY spend_date, platform DESC"
df=pd.read_sql(querytoexecute,conn)
print(df)
conn.close()