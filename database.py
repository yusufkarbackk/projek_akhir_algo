import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=8889,
    database="mydatabase"
)
mycursor = mydb.cursor()

nama = input('masukan nama buku: ')
date = datetime.datetime.now()

sql = "INSERT INTO books(nama_buku, waktu_masuk) VALUES ('{}', '{}')".format(nama, date)
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, 'record inserted')
