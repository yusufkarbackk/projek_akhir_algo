import mysql.connector
import datetime


def connect_sql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=8889,
        database="mydatabase"
    )


def insert_mahasiswa(nama, nim, prodi):
    mydb = connect_sql()
    mycursor = mydb.cursor()

    sql = "INSERT INTO users(name, nim, prodi) VALUES ('{}', {}, '{}')".format(
        nama, nim, prodi)

    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, 'record inserted')



