import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=8889,
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for i in mycursor:
    print(i)