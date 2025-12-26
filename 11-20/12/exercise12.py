import sqlite3
import pandas as pd
import os

db_name="exercise12.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS players(player_id INT, group_id INT)""")
# cursor.execute("""CREATE TABLE IF NOT EXISTS matches(match_id INT, first_player INT, second_player INT, first_score INT, second_score INT)""")
# conn.commit()

# player_data=[
#     (15,1),
#     (25,1),
#     (30,1),
#     (45,1),
#     (10,2),
#     (35,2),
#     (50,2),
#     (20,3),
#     (40,3)
# ]
# cursor.executemany("INSERT INTO players VALUES(?,?)",player_data)

# matches_data=[
#     (1,15,45,3,0),
#     (2,30,25,1,2),
#     (3,30,15,2,0),
#     (4,40,20,5,2),
#     (5,35,50,1,1)
# ]
# cursor.executemany("INSERT INTO matches VALUES(?,?,?,?,?)",matches_data)
# conn.commit()


queryexecute="WITH player_scores AS (SELECT first_player AS player_id, first_score AS score FROM matches UNION ALL SELECT second_player AS player_id, second_score AS score FROM matches), final_scores AS (SELECT p.group_id, ps.player_id, SUM(score) AS score FROM player_scores AS ps INNER JOIN players AS p ON p.player_id=ps.player_id GROUP BY p.group_id, ps.player_id), final_ranking AS (SELECT *, RANK() OVER (PARTITION BY group_id ORDER BY score DESC, player_id ASC) AS rn FROM final_scores) SELECT * FROM final_ranking WHERE rn=1"
df=pd.read_sql(queryexecute,conn)
print(df)
conn.close()