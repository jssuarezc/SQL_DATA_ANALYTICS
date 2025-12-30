import os
import sqlite3
import pandas as pd

db_name="exercise19.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS transactions(order_id INT, cust_id INT, order_date DATE, amount INT)""")
conn.commit()

cursor.execute("DELETE FROM transactions")
conn.commit()

transactions_data=[
    (1,1,'2020-01-15',150),
    (2,1,'2020-02-10',150),
    (3,2,'2020-01-16',150),
    (4,2,'2020-02-25',150),
    (5,3,'2020-01-10',150),
    (6,3,'2020-02-20',150),
    (7,4,'2020-01-20',150),
    (8,5,'2020-02-20',150)
]

cursor.executemany("INSERT INTO transactions VALUES(?,?,?,?)",transactions_data)
conn.commit()

querytoexec="SELECT strftime('%m',last_month.order_date) AS month_date, COUNT(DISTINCT last_month.cust_id) AS churned_customers FROM transactions AS last_month LEFT JOIN transactions AS this_month ON last_month.cust_id = this_month.cust_id AND strftime('%Y-%m',this_month.order_date)=strftime('%Y-%m', last_month.order_date, '+1 month') WHERE this_month.cust_id IS NULL GROUP BY month_date"
df=pd.read_sql(querytoexec,conn)
print(df)
conn.close()