import sqlite3
import os
import pandas as pd

db_name="exercise13.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

#
cursor.execute("""CREATE TABLE IF NOT EXISTS users(user_id INT, join_date DATE, favorite_brand VARCHAR(50))""")
cursor.execute("""CREATE TABLE IF NOT EXISTS orders(order_id INT, order_date DATE, item_id INT, buyer_id INT, seller_id INT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS items(item_id INT, item_brand VARCHAR(50))""")
conn.commit()

users_data=[
    (1,'2019-01-01','Lenovo'),
    (2,'2019-02-09','Samsung'),
    (3,'2019-01-19','LG'),
    (4,'2019-05-21','HP')
]
cursor.executemany("INSERT INTO users VALUES(?,?,?)",users_data)

items_data=[
    (1,'Samsung'),
    (2,'Lenovo'),
    (3,'LG'),
    (4,'HP')
]
cursor.executemany("INSERT INTO items VALUES(?,?)",items_data)

orders_data=[
    (1,'2019-08-01',4,1,2),
    (2,'2019-08-02',2,1,3),
    (3,'2019-08-03',3,2,3),
    (4,'2019-08-04',1,4,2),
    (5,'2019-08-04',1,3,4),
    (6,'2019-08-05',2,2,4)
]
cursor.executemany("INSERT INTO orders VALUES (?,?,?,?,?)",orders_data)
conn.commit()
#

querytoexec="WITH rnk_orders AS (SELECT *, RANK() OVER (PARTITION BY seller_id ORDER BY order_date ASC) AS rn FROM orders) SELECT u.user_id AS seller_id, CASE WHEN i.item_brand=u.favorite_brand THEN 'YES' ELSE 'NO' END AS item_fav_brand FROM users AS u LEFT JOIN rnk_orders AS ro ON ro.seller_id = u.user_id AND rn=2 LEFT JOIN items AS i ON i.item_id=ro.item_id"
df=pd.read_sql(querytoexec,conn)
print(df)
conn.close()