import pyodbc as db
import pandas as pd
conn = db.connect('Driver={SQL Server};'
                      'Server=ONUR\SQLEXPRESS01;'
                      'Database=Northwind;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
df = pd.read_sql_query('SELECT * FROM Employees', conn)
print(df)