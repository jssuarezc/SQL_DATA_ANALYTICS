import os
import sqlite3
import pandas as pd

db_name="exercise28.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS products(product_id VARCHAR(20), cost INT)""")
# cursor.execute("""CREATE TABLE IF NOT EXISTS customer_budget(customer_id INT, budget INT)""")

# conn.commit()

# products_data=[
#     ('P1',200),
#     ('P2',300),
#     ('P3',500),
#     ('P4',800)
# ]
# cursor.executemany("INSERT INTO products VALUES(?,?)",products_data)
# conn.commit()

# customer_data=[
#     (100,400),
#     (200,800),
#     (300,1500)
# ]
# cursor.executemany("INSERT INTO customer_budget VALUES(?,?)",customer_data)
# conn.commit()

querytoexec="WITH running_cost AS (SELECT *, SUM(cost) OVER(ORDER BY cost ASC)AS r_cost FROM products) SELECT customer_id, budget, COUNT(1) AS no_of_prod, string_agg(product_id,',') AS list_of_prod FROM customer_budget AS cb LEFT JOIN running_cost AS rc ON rc.r_cost <= cb.budget GROUP BY customer_id, budget"
df=pd.read_sql(querytoexec,conn)
print(df)
conn.close()