# Materi print, variabel, tipe data (angka, teks)
print("================================")
print("Program Menyapa Pengguna")
print("================================")

# Input
input_nama = input("Masukkan Nama Anda: ") # tipe data teks (string)
input_umur = input("Masukkan Umur Anda: ") # tipe data teks (string) walau konteks umur itu angka, tapi input() akan mengembalikan tipe data string

# Proses
sapa = "Halo " + input_nama + "\nWah, umur kamu " + input_umur + " tahun, ya!\n" + "Senang berkenalan denganmu dan Selamat Datang di Program Belajar Python Dasar!" 

# Output
print(sapa)
