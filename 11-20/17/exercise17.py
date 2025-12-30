import sqlite3
import pandas as pd
import os


db_name="exercise17.db"
conn=sqlite3.connect(db_name)
cursor= conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS orders(order_id INT, customer_id INT, product_id INT)""")
# cursor.execute("""CREATE TABLE IF NOT EXISTS products(id INT, name VARCHAR(10))""")

# conn.commit()

# orders_add=[
#     (1, 1, 1),
# (1, 1, 2),
# (1, 1, 3),
# (2, 2, 1),
# (2, 2, 2),
# (2, 2, 4),
# (3, 1, 5)
# ]

# cursor.executemany("INSERT INTO orders VALUES(?,?,?)",orders_add)

# products_add=[
#     (1, 'A'),
# (2, 'B'),
# (3, 'C'),
# (4, 'D'),
# (5, 'E')
# ]
# cursor.executemany("INSERT INTO products VALUES(?,?)",products_add)
# conn.commit()

#"|| ||" concatenates strings in SQLITE3!!!

querytoexecute="SELECT pr1.name || ' ' || pr2.name AS pair, COUNT(1) AS purchase_freq FROM orders AS o1 INNER JOIN orders AS o2 ON o1.order_id = o2.order_id INNER JOIN products AS pr1 ON pr1.id=o1.product_id INNER JOIN products AS pr2 ON pr2.id= o2.product_id WHERE o1.product_id < o2.product_id GROUP BY pr1.name, pr2.name"
df=pd.read_sql(querytoexecute,conn)
print(df)
conn.close()