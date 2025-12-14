import sqlite3
import pandas as pd
import os

db_name="exercise04.db"
conn = sqlite3.connect(db_name)
cursor= conn.cursor()


# cursor.execute("""CREATE TABLE IF NOT EXISTS entries(
#                name VARCHAR(20),
#                address VARCHAR(20),
#                email VARCHAR(20),
#                floor INT,
#                resources VARCHAR(10))""")
# conn.commit()

# datatofill=[
#     ('A','Bangalore','A@gmail.com',1,'CPU'),
#     ('A','Bangalore','A1@gmail.com',1,'CPU'),
#     ('A','Bangalore','A2@gmail.com',2,'DESKTOP'),
#     ('B','Bangalore','B@gmail.com',2,'DESKTOP'),
#     ('B','Bangalore','B1@gmail.com',2,'DESKTOP'),
#     ('B','Bangalore','B2@gmail.com',1,'MONITOR')
# ]
# cursor.executemany("INSERT INTO entries(name,address,email,floor,resources) VALUES(?,?,?,?,?)",datatofill)
# conn.commit()


querytoexecute="WITH distinct_resources AS(SELECT DISTINCT name, resources FROM entries), AGG_RESOURCES AS (SELECT name, STRING_AGG(resources,',') AS used_resources FROM distinct_resources GROUP BY name), total_visits AS (SELECT name, COUNT(1) AS total_visits ,STRING_AGG(resources,',') AS resources_used FROM entries GROUP BY name), floor_visit AS (SELECT name, floor, COUNT(1) AS no_floor_visited, RANK() OVER(PARTITION BY name ORDER BY COUNT(1) DESC) AS rn FROM entries GROUP BY name, floor) SELECT fv.name, fv.floor AS most_visited_floor,tv.total_visits,ar.used_resources FROM floor_visit AS fv INNER JOIN total_visits AS tv ON fv.name=tv.name INNER JOIN agg_resources AS ar ON fv.name=ar.name WHERE rn=1"
df=pd.read_sql(querytoexecute,conn)
print(df)
conn.close()
