file = open('names.txt', 'a+')
nama = input('Masukan nama anda: ')

file.write(nama + "\n")
file.close()

