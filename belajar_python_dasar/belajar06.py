# Materi: Function (fungsi) dan parameter
# Studi Kasus: Pecah program lama jadi potongan fungsi

# proses
def sapa_pengguna(nama, umur):
    sapa = "Halo " + nama + "\nWah, umur kamu " + umur + " tahun, ya!\n" + "Senang berkenalan denganmu dan Selamat Datang di Program Belajar Python Dasar!" 
    return sapa

# input
input_nama = input("Masukkan Nama Anda: ")
input_umur = input("Masukkan Umur Anda: ")

# proses
program_sapa = sapa_pengguna(input_nama, input_umur)

# output
print(program_sapa)
