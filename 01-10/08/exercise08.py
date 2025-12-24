import sqlite3
import os
import pandas as pd

db_name = "exercise08.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS friend (pid INT, fid INT);")
# cursor.execute("CREATE TABLE IF NOT EXISTS person (PersonID INT, Name VARCHAR(50), Score INT);")
# conn.commit()

# friend_data = [
#     (1, 2), (1, 3), (2, 1), (2, 3), 
#     (3, 5), (4, 2), (4, 3), (4, 5)
# ]
# cursor.executemany("INSERT INTO friend (pid, fid) VALUES (?, ?);", friend_data)

# person_data = [
#     (1, 'Alice', 88),
#     (2, 'Bob', 11),
#     (3, 'Devis', 27),
#     (4, 'Tara', 45),
#     (5, 'John', 63)
# ]
# cursor.executemany("INSERT INTO person (PersonID, Name, Score) VALUES (?, ?, ?);", person_data)
# conn.commit()

queryexec="WITH score_details AS(SELECT f.pid, SUM(p.score) AS total_friend_score, COUNT(1) AS no_of_friends FROM friend AS f INNER JOIN person AS p ON f.fid=p.personid GROUP BY f.pid HAVING SUM(p.score) > 100) SELECT s.*,p.name AS person_name FROM person AS p INNER JOIN score_details AS s ON p.personid=s.pid"
df=pd.read_sql(queryexec,conn)
print(df)
conn.close()