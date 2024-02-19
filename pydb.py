import pyodbc
import json
import pandas as pd

json_file = open('settings.json')
settings_file = json.load(json_file)["Database_parameter"]
json_file.close()

driver = settings_file['Driver']
server = settings_file['Server']
database = settings_file['Database']
username = settings_file['Username']
password = settings_file['Password']
trusted_connection = settings_file['Trusted_Connection']
encrypt = settings_file['Encrypt']


cnxn = pyodbc.connect("Driver="+ driver +";Server="+ server +";Database="\
                      + database +";User Id="+ username +";Password="+ password \
                      +";Trusted_Connection="+ trusted_connection +";Encrypt="+ encrypt +";")
cursor = cnxn.cursor()
cursor.execute('Select top 5 * from Orders')

df = pd.DataFrame(cursor,columns=None)

print(df[0])

cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()

cnxn.close()
