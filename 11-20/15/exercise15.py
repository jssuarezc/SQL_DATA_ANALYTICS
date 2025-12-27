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

querytoexecute="WITH r_cte AS (SELECT MIN(period_start) AS dates, MAX(period_end) AS max_date FROM sales UNION ALL SELECT dateadd(day,1,dates) AS dates, max_date FROM r_cte WHERE dates < max_date) SELECT product_id, YEAR(dates) AS report_year, SUM(average_daily_sales) AS total_amount FROM r_cte INNER JOIN sales ON dates BETWEEN period_start AND period_end GROUP BY product_id, YEAR(dates) ORDER BY product_id, YEAR(dates) OPTION (maxrecursion 1000)"
df=pd.read_sql(querytoexecute,conn)
print(df)
conn.close()