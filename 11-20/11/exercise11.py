import sqlite3
import os
import pandas as pd

db_name="exercise11.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS emp(emp_id INT, emp_name VARCHAR(20), department_id INT, salary INT, manager_id INT, emp_age INT)""")
# conn.commit()

# emp_data=[
#     (1, 'Ankit', 100,10000, 4, 39),
#     (2, 'Mohit', 100, 15000, 5, 48),
#     (3, 'Vikas', 100, 10000,4,37),
#     (4, 'Rohit', 100, 5000, 2, 16),
#     (5, 'Mudit', 200, 12000, 6,55),
#     (6, 'Agam', 200, 12000,2, 14),
#     (7, 'Sanjay', 200, 9000, 2,13),
#     (8, 'Ashish', 200,5000,2,12),
#     (9, 'Mukesh',300,6000,6,51),
#     (10, 'Rakesh',300,7000,6,50)    
# ]
# cursor.executemany("INSERT INTO emp VALUES(?,?,?,?,?,?)",emp_data)
# conn.commit()

queryexecute="WITH ordered_salaries AS(SELECT department_id, salary, ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary) AS rn, COUNT(*) OVER (PARTITION BY department_id)AS cnt FROM emp) SELECT department_id, AVG(salary) AS median_salary FROM ordered_salaries WHERE rn IN((cnt+1)/2,(cnt+2)/2) GROUP BY department_id"
df=pd.read_sql(queryexecute,conn)
print(df)
conn.close()