import sqlite3
import pandas as pd
from datetime import datetime,timedelta

today_date_str = '2022-01-03'
n=3
today_dt= datetime.strptime(today_date_str,'%Y-%m-%d')

#Replicating T-SQL in SQLite:

days_to_next_sunday= (6- today_dt.weekday())
if days_to_next_sunday <=0:
    days_to_next_sunday +=7

result_date = today_dt +timedelta(days=days_to_next_sunday) + timedelta(weeks=n-1)


conn=sqlite3.connect("exercise06.db")
query=f"SELECT '{result_date.date()}' AS calculated_date"
df = pd.read_sql(query,conn)
print(df)
conn.close()