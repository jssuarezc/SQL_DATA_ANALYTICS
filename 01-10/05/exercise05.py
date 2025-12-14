import sqlite3
import os
import pandas as pd

db_name="exercise05.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()


# cursor.execute("""CREATE TABLE IF NOT EXISTS emp_compensation(
#                emp_id INT,
#                salary_component_type VARCHAR(20),
#                val INT)""")
# conn.commit()

# dataentry = [
#     (1,'salary',10000),
#     (1,'bonus',5000),
#     (1,'hike_percent',10),
#     (2,'salary',15000),
#     (2,'bonus',7000),
#     (2,'hike_percent',8),
#     (3,'salary',12000),
#     (3,'bonus',6000),
#     (3,'hike_percent',7)
# ]
# cursor.executemany("INSERT INTO emp_compensation(emp_id,salary_component_type,val) VALUES(?,?,?)",dataentry)
# conn.commit()

queryexecute="SELECT emp_id, SUM(CASE WHEN salary_component_type='salary' THEN val END) AS salary, SUM(CASE WHEN salary_component_type='bonus' THEN val END) AS bonus, SUM(CASE WHEN salary_component_type='hike_percent' THEN val END) AS hike_percent FROM emp_compensation GROUP BY emp_id"
df=pd.read_sql(queryexecute,conn)
print(df)
conn.close()
