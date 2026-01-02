import os
import sqlite3
import pandas as pd

db_name = "exercise30.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS students(
#     studentid INT,
#     studentname TEXT,
#     subject TEXT,
#     marks INT,
#     testid INT,
#     testdate DATE
# )""")
# conn.commit()

# students_data = [
#     (2, 'Max Ruin', 'Subject1', 63, 1, '2022-01-02'),
#     (3, 'Arnold', 'Subject1', 95, 1, '2022-01-02'),
#     (4, 'Krish Star', 'Subject1', 61, 1, '2022-01-02'),
#     (5, 'John Mike', 'Subject1', 91, 1, '2022-01-02'),
#     (4, 'Krish Star', 'Subject2', 71, 1, '2022-01-02'),
#     (3, 'Arnold', 'Subject2', 32, 1, '2022-01-02'),
#     (5, 'John Mike', 'Subject2', 61, 2, '2022-11-02'),
#     (1, 'John Deo', 'Subject2', 60, 1, '2022-01-02'),
#     (2, 'Max Ruin', 'Subject2', 84, 1, '2022-01-02'),
#     (2, 'Max Ruin', 'Subject3', 29, 3, '2022-01-03'),
#     (5, 'John Mike', 'Subject3', 98, 2, '2022-11-02')
# ]

# cursor.executemany("INSERT INTO students VALUES(?,?,?,?,?,?)", students_data)
# conn.commit()

firstq = "WITH avg_cte AS (SELECT subject, AVG(marks) AS avg_marks FROM students GROUP BY subject) SELECT s.*, ac.* FROM students s INNER JOIN avg_cte ac ON s.subject = ac.subject WHERE s.marks > ac.avg_marks;"
secondq = "SELECT COUNT(DISTINCT CASE WHEN marks > 90 THEN studentid ELSE NULL END) * 1.0 / COUNT(DISTINCT studentid) * 100 AS perc FROM students;"
thirdq = "SELECT subject, SUM(CASE WHEN rnk_desc = 2 THEN marks ELSE NULL END) AS second_highest_marks, SUM(CASE WHEN rnk_asc = 2 THEN marks ELSE NULL END) AS second_lowest_marks FROM (SELECT subject, marks, RANK() OVER(PARTITION BY subject ORDER BY marks ASC) AS rnk_asc, RANK() OVER(PARTITION BY subject ORDER BY marks DESC) AS rnk_desc FROM students) A GROUP BY subject;"
fourthq = "SELECT *, CASE WHEN marks > prev_marks THEN 'inc' WHEN marks < prev_marks THEN 'dec' ELSE NULL END AS statys FROM (SELECT *, LAG(marks, 1) OVER(PARTITION BY studentid ORDER BY testdate, subject) AS prev_marks FROM students) A;"
df = pd.read_sql(fourthq, conn)
print(df)
conn.close()