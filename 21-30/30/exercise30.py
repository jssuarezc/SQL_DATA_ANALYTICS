import os
import sqlite3
import pandas as pd

db_name = "exercise30.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    studentid INT,
    studentname TEXT,
    subject TEXT,
    marks INT,
    testid INT,
    testdate DATE
)""")
conn.commit()

students_data = [
    (2, 'Max Ruin', 'Subject1', 63, 1, '2022-01-02'),
    (3, 'Arnold', 'Subject1', 95, 1, '2022-01-02'),
    (4, 'Krish Star', 'Subject1', 61, 1, '2022-01-02'),
    (5, 'John Mike', 'Subject1', 91, 1, '2022-01-02'),
    (4, 'Krish Star', 'Subject2', 71, 1, '2022-01-02'),
    (3, 'Arnold', 'Subject2', 32, 1, '2022-01-02'),
    (5, 'John Mike', 'Subject2', 61, 2, '2022-11-02'),
    (1, 'John Deo', 'Subject2', 60, 1, '2022-01-02'),
    (2, 'Max Ruin', 'Subject2', 84, 1, '2022-01-02'),
    (2, 'Max Ruin', 'Subject3', 29, 3, '2022-01-03'),
    (5, 'John Mike', 'Subject3', 98, 2, '2022-11-02')
]

cursor.executemany("INSERT INTO students VALUES(?,?,?,?,?,?)", students_data)
conn.commit()

firstq = "WITH avg_cte AS (SELECT subject, AVG(marks) AS avg_marks FROM students GROUP BY subject) SELECT s.*, ac.* FROM students s INNER JOIN avg_cte ac ON s.subject = ac.subject WHERE s.marks > ac.avg_marks;"
secondq = "SELECT COUNT(DISTINCT CASE WHEN marks > 90 THEN studentid ELSE NULL END) * 1.0 / COUNT(DISTINCT studentid) * 100 AS perc FROM students;"
thirdq = "SELECT * FROM students"
fourthq = "SELECT * FROM students"
df = pd.read_sql(secondq, conn)
print(df)
conn.close()