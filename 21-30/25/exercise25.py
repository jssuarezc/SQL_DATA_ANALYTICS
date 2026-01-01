import os
import sqlite3
import pandas as pd

db_name="exercise25.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS exams(student_id INT, subject VARCHAR(20), marks INT)""")
# conn.commit()

# cursor.execute("DELETE FROM exams")
# conn.commit()

# exams_data=[
#     (1,'Chemistry',91),
#     (1,'Physics',91),
#     (2,'Chemistry',80),
#     (2,'Physics',90),
#     (3,'Chemistry',80),
#     (4,'Chemistry',71),
#     (4,'Physics',54)
# ]
# cursor.executemany("INSERT INTO exams VALUES(?,?,?)",exams_data)
# conn.commit()

querytoexec="SELECT student_id FROM exams WHERE subject in ('Chemistry','Physics') GROUP BY student_id HAVING COUNT(DISTINCT subject)=2 AND COUNT(DISTINCT marks)=1"
df=pd.read_sql(querytoexec,conn)
print(df)
conn.close()