# Materi: Function (fungsi) dan parameter
# Studi Kasus: Pecah program lama jadi potongan fungsi

def sapa_pengguna(nama, umur):
    print("Halo " + nama + ",")
    print("Wah, umur kamu " + umur + " tahun, ya!")
    print("Senang berkenalan denganmu dan Selamat Datang di Program Belajar Python Dasar!")

input_nama = input("Masukkan Nama Anda: ")
input_umur = input("Masukkan Umur Anda: ")

sapa_pengguna(input_nama, input_umur)
