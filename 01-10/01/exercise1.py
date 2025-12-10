import sqlite3
import pandas as pd
import os

db_name="question1.db"

conn = sqlite3.connect(db_name)
cursor=conn.cursor()

# #Database creation--------
#conn = sqlite3.connect(db_name)
#cursor=conn.cursor()

# print("Creating table...")
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS icc_world_cup(
#         Team_1 VARCHAR(20),
#         Team_2 VARCHAR(20),
#         Winner VARCHAR(20))
# """)
# conn.commit()

# #Add data to our database-------------
# teams= [
#     ('India','SL','India'),
#     ('SL','Aus','Aus'),
#     ('SA','Eng','Eng'),
#     ('Eng','NZ','NZ'),
#     ('Aus','India','India'),            
# ]
# cursor.executemany("INSERT INTO icc_world_cup(Team_1,Team_2,Winner) VALUES(?,?,?)",teams)
# conn.commit()
# print("Data inserted successfully.")

#Execute query
query="SELECT * from icc_world_cup"
df=pd.read_sql(query,conn)
print("Query result:")
print(df)

query2="select team_name, count(1) as no_of_matches_played, sum(win_flag) as no_matches_won,count(1)-sum(win_flag) as no_matches_lost from (select Team_1 as team_name, case when Team_1=winner then 1 else 0 end as win_flag from icc_world_cup union " \
"all select Team_2 as team_name, case when Team_2=winner then 1 else 0 end as win_flag from icc_world_cup) A group by team_name ORDER BY no_matches_won desc"
df2=pd.read_sql(query2,conn)
print(df2)
conn.close