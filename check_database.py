import sqlite3

connection = sqlite3.connect('urls.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM urls")
records = cursor.fetchall()
print("saved urls records:")
for record in records:
    print(record)