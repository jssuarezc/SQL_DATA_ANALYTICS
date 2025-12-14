import sqlite3
import pandas as pd
import os

db_name="question2.db"

conn = sqlite3.connect(db_name)
cursor=conn.cursor()

# print("Creating table")
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS emp(
#                emp_id INT,
#                emp_name VARCHAR(10),
#                salary INT,
#                manager_id INT
#     )
# """)
# conn.commit()

# dataemp = [
#     (1,'Ankit',10000,4),
#     (2,'Mohit',15000,5),
#     (3,'Vikas',10000,4),
#     (4,'Rohit',5000,2),
#     (5,'Mudit',12000,6),
#     (6,'Agam',12000,2),
#     (7,'Sanjay',9000,2),
#     (8,'Ashish',5000,2)
# ]
# cursor.executemany("INSERT INTO emp(emp_id, emp_name,salary,manager_id) VALUES(?,?,?,?)",dataemp)
# conn.commit()
# print("Data added successfully")

#Execute query
query="SELECT e.emp_id, e.emp_name, m.emp_name AS manager_name, e.salary, m.salary AS mger_salary FROM emp AS e INNER JOIN emp AS m ON e.manager_id = m.emp_id where e.salary > m.salary"
df=pd.read_sql(query,conn)
print("Query result:")
print(df)
conn.close()
