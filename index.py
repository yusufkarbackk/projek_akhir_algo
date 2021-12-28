import db_helper

nama = input('masukan nama anda: ')
nim = int(input('masukan nim: '))
prodi = input('masukan prodi: ')

db_helper.insert_mahasiswa(nama, nim, prodi)
