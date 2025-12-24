import sqlite3
import os
import pandas as pd

db_name="exercise09.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS emp(emp_id INT, emp_name VARCHAR(10),department_id INT,salary INT, manager_id INT);""")
# conn.commit()

# emp_data=[
#     (1,'Ankit',100,10000,4),
#     (2,'Mohit',100,15000,5),
#     (3,'Vikas',100,10000,4),
#     (4,'Rohit',100,5000,2),
#     (5,'Mudit',200,12000,6),
#     (6,'Agam',200,12000,2),
#     (7,'Sanjay',200,9000,2),
#     (8,'Ashish',200,5000,2)
# ]
# cursor.executemany("INSERT INTO emp(emp_id, emp_name,department_id,salary, manager_id) VALUES(?,?,?,?,?)",emp_data)
# conn.commit()


queryexec="SELECT department_id,avg(salary) FROM emp WHERE salary>10000 GROUP BY department_id HAVING avg(salary)>12000;"
df=pd.read_sql(queryexec,conn)
print(df)
conn.close()