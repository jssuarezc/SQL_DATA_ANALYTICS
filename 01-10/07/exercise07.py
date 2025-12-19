import sqlite3
import pandas as pd
import os

db_name="exercise07.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

# with open("Day7_data.txt", 'r') as sql_file:
#     sql_script = sql_file.read()

# # Executing table creation and inserts at once
# try:
#     cursor.executescript(sql_script)
#     conn.commit()
#     print("Database populated successfully!")
# except sqlite3.Error as e:
#     print(f"An error occurred: {e}")

# #Verify if table was created
# df = pd.read_sql("SELECT * FROM orders LIMIT 10", conn)
# print(df)
# conn.close()

queryexec = """
WITH product_wise_sales AS (
    SELECT product_id, SUM(sales) AS product_sales 
    FROM orders GROUP BY product_id
), 
cal_sales AS (
    SELECT 
        product_id, 
        product_sales, 
        SUM(product_sales) OVER (ORDER BY product_sales DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_sales, 
        0.8 * SUM(product_sales) OVER () AS total_sales 
    FROM product_wise_sales
) 
SELECT * FROM cal_sales WHERE running_sales <= total_sales
"""

df = pd.read_sql(queryexec, conn)
print(df)
conn.close()