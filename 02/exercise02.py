import sqlite3
import pandas as pd
import os

db_name="question2.db"
#create db - remember to leave conn and cursor duplicate so code can run!!
conn = sqlite3.connect(db_name)
cursor=conn.cursor()

print("Creating table")
cursor.execute()
conn.commit

#add data

