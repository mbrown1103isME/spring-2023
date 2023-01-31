# List everything in the students table
import sqlite3
from printit import printit

con = sqlite3.connect('data/students.db')
cur = con.cursor()

# All students
sql = "SELECT * FROM student"
printit(cur, sql)

con.close()
