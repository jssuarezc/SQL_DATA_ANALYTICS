import os
import sqlite3
import pandas as pd

db_name="exercise23.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS bms(seat_no INT,is_empty VARCHAR(10))""")
# conn.commit()

# bms_data=[
#     (1,'N'),
#     (2,'Y'),
#     (3,'N'),
#     (4,'Y'),
#     (5,'Y'),
#     (6,'Y'),
#     (7,'N'),
#     (8,'Y'),
#     (9,'Y'),
#     (10,'Y'),
#     (11,'Y'),
#     (12,'N'),
#     (13,'Y'),
#     (14,'Y')
# ]
# conn.commit()

# cursor.executemany("INSERT INTO bms VALUES(?,?)",bms_data)
# conn.commit()

first_method="SELECT * FROM (SELECT * ,LAG(is_empty,1) OVER(ORDER BY seat_no) AS prev_1, LAG(is_empty,2) OVER(ORDER BY seat_no) AS prev_2, LEAD(is_empty,1) OVER(ORDER BY seat_no) AS next_1, LEAD(is_empty,2) OVER (ORDER BY seat_no) AS next_2 FROM bms) A WHERE is_empty='Y' AND prev_1='Y' and prev_2='Y' OR(is_empty='Y' and prev_1='Y' and next_1='Y') OR (is_empty='Y' and next_1='Y' and next_2='Y')"
second_method="SELECT * FROM (SELECT *, SUM(CASE WHEN is_empty = 'Y' THEN 1 ELSE 0 END) OVER (ORDER BY seat_no ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS prev_2, SUM(CASE WHEN is_empty = 'Y' THEN 1 ELSE 0 END) OVER (ORDER BY seat_no ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS prev_next_1, SUM(CASE WHEN is_empty = 'Y' THEN 1 ELSE 0 END) OVER (ORDER BY seat_no ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING) AS next_2 FROM BMS) A WHERE prev_2 = 3 OR prev_next_1 = 3 OR next_2 = 3"
df=pd.read_sql(second_method,conn)
print(df)
conn.close()

# third_method="SELECT * FROM bms"
# df=pd.read_sql(third_method,conn)
# print(df)
# conn.close()