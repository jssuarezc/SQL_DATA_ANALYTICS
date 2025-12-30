import os
import sqlite3
import pandas as pd

db_name="exercise16.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS users(user_id INT, name VARCHAR(20),join_date DATE)""")
# cursor.execute("""CREATE TABLE IF NOT EXISTS events(user_id INT, type VARCHAR(10),access_date DATE)""")
# conn.commit()

# users_info=[
#     (1, 'Jon', '2020-02-14'),
#     (2, 'Jane', '2020-02-14'), 
#     (3, 'Jill', '2020-02-15'), 
#     (4, 'Josh', '2020-02-15'), 
#     (5, 'Jean', '2020-02-16'), 
#     (6, 'Justin', '2020-02-17'),
#     (7, 'Jeremy', '2020-02-18')
# ]
# cursor.executemany("INSERT INTO users VALUES(?,?,?)",users_info)

# events_info=[
#     (1, 'Music','2020-03-01'), # Changed from 'Pay' to 'Music' to match your WHERE clause
#     (2, 'Music','2020-03-02'), 
#     (2, 'P','2020-03-12'),
#     (3, 'Music','2020-03-15'), 
#     (4, 'Music','2020-03-15'), 
#     (1, 'P','2020-03-16'), 
#     (3, 'P','2020-03-22')
# ]
# cursor.executemany("INSERT INTO events VALUES(?,?,?)",events_info)
# conn.commit()

stringtoe = "SELECT COUNT(DISTINCT u.user_id) AS total_users, COUNT(DISTINCT CASE WHEN julianday(e.access_date) - julianday(u.join_date) <= 30 THEN u.user_id END) AS retained_users, 100.0 * COUNT(DISTINCT CASE WHEN julianday(e.access_date) - julianday(u.join_date) <= 30 THEN u.user_id END) / COUNT(DISTINCT u.user_id) AS retention_rate FROM users AS u LEFT JOIN events AS e ON u.user_id = e.user_id AND e.type = 'P' WHERE u.user_id IN (SELECT user_id FROM events WHERE type = 'Music')"
df=pd.read_sql(stringtoe,conn)
print(df)
conn.close()