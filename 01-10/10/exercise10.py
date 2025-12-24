import sqlite3
import pandas as pd
import os

db_name="exercise10.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Trips (
#     id INT, 
#     client_id INT, 
#     driver_id INT, 
#     city_id INT, 
#     status VARCHAR(50), 
#     request_at VARCHAR(50)
# );
# """)
# cursor.execute("CREATE TABLE IF NOT EXISTS Users (users_id INT, banned VARCHAR(50), role VARCHAR(50));")
# conn.commit()

# trips_data = [
#     (1, 1, 10, 1, 'completed', '2013-10-01'),
#     (2, 2, 11, 1, 'cancelled_by_driver', '2013-10-01'),
#     (3, 3, 12, 6, 'completed', '2013-10-01'),
#     (4, 4, 13, 6, 'cancelled_by_client', '2013-10-01'),
#     (5, 1, 10, 1, 'completed', '2013-10-02'),
#     (6, 2, 11, 6, 'completed', '2013-10-02'),
#     (7, 3, 12, 6, 'completed', '2013-10-02'),
#     (8, 2, 12, 12, 'completed', '2013-10-03'),
#     (9, 3, 10, 12, 'completed', '2013-10-03'),
#     (10, 4, 13, 12, 'cancelled_by_driver', '2013-10-03')
# ]
# cursor.executemany("INSERT INTO Trips VALUES (?, ?, ?, ?, ?, ?)", trips_data)
# users_data = [
#     (1, 'No', 'client'), (2, 'Yes', 'client'), (3, 'No', 'client'), (4, 'No', 'client'),
#     (10, 'No', 'driver'), (11, 'No', 'driver'), (12, 'No', 'driver'), (13, 'No', 'driver')
# ]
# cursor.executemany("INSERT INTO Users VALUES (?, ?, ?)", users_data)
# conn.commit()

queryread="SELECT request_at, COUNT(CASE WHEN status IN('cancelled_by_client','cancelled_by_driver')THEN 1 ELSE NULL END) AS cancelled_trip_count, COUNT(1) AS total_trips, 1.0* COUNT(CASE WHEN status IN('cancelled_by_client','cancelled_by_driver')THEN 1 ELSE NULL END)/COUNT(1)*100 AS cancelled_percent FROM trips AS t INNER JOIN users AS c ON t.client_id=c.users_id INNER JOIN users AS d ON t.driver_id=d.users_id WHERE c.banned='No' AND d.banned='No' GROUP BY request_at;"
df=pd.read_sql(queryread,conn)
print(df)
conn.close()