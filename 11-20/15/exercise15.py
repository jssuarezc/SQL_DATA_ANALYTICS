import os
import sqlite3
import pandas as pd

db_name="exercise15.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS sales(product_id INT, period_start DATE, period_end DATE, average_daily_sales INT)""")
# conn.commit()

# string_db=[
#     (1,'2019-01-25','2019-02-28',100),
#     (2,'2018-12-01','2020-01-01',10),
#     (3,'2019-12-01','2020-01-31',1)
# ]

# cursor.executemany("INSERT INTO sales VALUES(?,?,?,?)",string_db)
# conn.commit()

querytoexecute="WITH RECURSIVE r_cte AS (SELECT MIN(period_start) AS dates, MAX(period_end) AS max_date FROM sales UNION ALL SELECT date(dates, '+1 day'), max_date FROM r_cte WHERE dates < max_date) SELECT s.product_id, strftime('%Y', r.dates) AS report_year, SUM(s.average_daily_sales) AS total_amount FROM r_cte r INNER JOIN sales s ON r.dates BETWEEN s.period_start AND s.period_end GROUP BY s.product_id, report_year ORDER BY s.product_id, report_year;"
df=pd.read_sql(querytoexecute,conn)
print(df)
conn.close()