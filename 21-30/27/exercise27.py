import os
import sqlite3
import pandas as pd

db_name="exercise27.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS company_users(company_id INT, user_id INT, language VARCHAR(20))""")
# conn.commit()

# company_data=[
#     (1,1,'English'),
#     (1,1,'German'),
#     (1,2,'English'),
#     (1,3,'German'),
#     (1,3,'English'),
#     (1,4,'English'),
#     (2,5,'English'),
#     (2,5,'German'),
#     (2,5,'Spanish'),
#     (2,6,'German'),
#     (2,6,'Spanish'),
#     (2,7,'English')
# ]
# cursor.executemany("INSERT INTO company_users VALUES(?,?,?)",company_data)
# conn.commit()

querytoexec="SELECT company_id, COUNT(1) FROM (SELECT company_id, user_id FROM company_users WHERE LANGUAGE IN ('English','German')GROUP BY company_id, user_id HAVING COUNT(1)=2) AS a GROUP BY company_id HAVING COUNT(1) >=2"
df=pd.read_sql(querytoexec,conn)
print(df)
conn.close()