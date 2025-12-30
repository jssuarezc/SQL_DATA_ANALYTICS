import os
import sqlite3
import pandas as pd

db_name="exercise21.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS billings(emp_name VARCHAR(10), bill_date DATE, bill_rate INT)""")
# cursor.execute("""CREATE TABLE IF NOT EXISTS HoursWorked(emp_name VARCHAR(20), work_date DATE, bill_hrs INT)""")
# conn.commit()

# cursor.execute("DELETE FROM billings")
# conn.commit()

# billings_data=[
#     ('Sachin','01-JAN-1990',25),
#     ('Sehwag' ,'01-JAN-1989', 15),
#     ('Dhoni' ,'01-JAN-1989', 20),
#     ('Sachin' ,'05-Feb-1991', 30)
# ]
# conn.commit()

# hw_data=[
#     ('Sachin', '01-JUL-1990' ,3),
#     ('Sachin', '01-AUG-1990', 5),
#     ('Sehwag','01-JUL-1990', 2),
#     ('Sachin','01-JUL-1991', 4)
# ]

# cursor.executemany("INSERT INTO billings VALUES(?,?,?)",billings_data)
# cursor.executemany("INSERT INTO HoursWorked VALUES(?,?,?)",hw_data)
# conn.commit()

querytoexec="WITH date_range AS(SELECT *,LEAD(date(bill_date,'-1 day'),1,'9999-12-31') OVER(PARTITION BY emp_name ORDER BY bill_date ASC) AS bill_date_end FROM billings) SELECT hw.emp_name,SUM(dr.bill_rate * hw.bill_hrs) AS total_billed FROM date_range AS dr INNER JOIN HoursWorked AS hw ON hw.emp_name=dr.emp_name AND hw.work_date BETWEEN dr.bill_date AND dr.bill_date_end GROUP BY hw.emp_name"
df=pd.read_sql(querytoexec,conn)
print(df)
conn.close()