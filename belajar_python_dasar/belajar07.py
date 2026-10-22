# Materi: Baca Tulis File (File Handling)
# Studi Kasus: Programm Membaca dan Menulis File

# Read file
# Contoh tidak menggunakan mekanisme buka tutup file ototmatis (with ... as ...)
def read_file(file_path):
    try:
        file = open(file_path, "r")
        content = file.read()
        print("Isi File:")
        print(content)
        file.close()
    except FileNotFoundError:
        print(f"File '{file_path}' tidak ditemukan.")
        

# Write file
# # Contoh menggunakan mekanisme buka tutup file ototmatis (with ... as ...)
def write_file(file_path, content):
    try:
        with open(file_path, "a") as file:
            file.write(content)
            print(f"Berhasil menulis ke file: {file_path}")
    except FileNotFoundError:
        print(f"File '{file_path}' tidak ditemukan.")
        
        
# Perbedaan antara read_file() dan write_file() dalam penggunaan mekanisme buka tutup file otomatis (with ... as ...) 
# write_file() lebih aman dan bersih dari kesalahan karena file akan otomatis ditutup setelah blok with selesai dieksekusi,
# sedangkan read_file() memerlukan pemanggilan file.close() secara manual, yang bisa menyebabkan kebocoran sumber daya jika lupa menutup file atau
# jika terjadi error sebelum file.close() dipanggil.

# Penggunaan with ... as ... tidak terbatas pada file handling saja, tetapi juga dapat digunakan untuk mengelola sumber daya lain 
# seperti koneksi jaringan, database, atau objek lain yang memerlukan pembersihan setelah digunakan.

file_path = input("Masukkan path file yang ingin dimodifikasi: ")
content_to_write = input("Masukkan isi file yang ingin ditulis: ")

write_file(file_path, content_to_write)
read_file(file_path)