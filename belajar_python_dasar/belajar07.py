# Materi: Baca Tulis File (File Handling)
# Studi Kasus: Programm Membaca dan Menulis File

# Proses
# Read file
# Contoh tidak menggunakan mekanisme buka tutup file ototmatis (with ... as ...)
def read_file(file_path):
    try:
        file = open(file_path, "r")
        content = file.read()
        formatted_content = "Hasil Baca File:\n" + content
        file.close()
        return formatted_content
    except FileNotFoundError:
        pesan_gagal = f"File '{file_path}' tidak ditemukan."
        return pesan_gagal        

# Proses
# Write file
# # Contoh menggunakan mekanisme buka tutup file ototmatis (with ... as ...)
def write_file(file_path, content):
    try:
        with open(file_path, "w") as file:
            file.write(content)
            pesan_berhasil = f"Berhasil menulis ke file: {file_path}"
            return pesan_berhasil
    except FileNotFoundError:
        pesan_gagal = f"File '{file_path}' tidak ditemukan."
        return pesan_gagal

# Perbedaan antara read_file() dan write_file() dalam penggunaan mekanisme buka tutup file otomatis (with ... as ...) 
# write_file() lebih aman dan bersih dari kesalahan karena file akan otomatis ditutup setelah blok with selesai dieksekusi,
# sedangkan read_file() memerlukan pemanggilan file.close() secara manual, yang bisa menyebabkan kebocoran sumber daya jika lupa menutup file atau
# jika terjadi error sebelum file.close() dipanggil.

# Penggunaan with ... as ... tidak terbatas pada file handling saja, tetapi juga dapat digunakan untuk mengelola sumber daya lain 
# seperti koneksi jaringan, database, atau objek lain yang memerlukan pembersihan setelah digunakan.


# input
file_path = input("Masukkan path file yang ingin dimodifikasi: ")
content_to_write = input("Masukkan isi file yang ingin ditulis: ")

# proses
hasil_penulisan = write_file(file_path, content_to_write)
hasil_baca = read_file(file_path)

# output
print("================================" + "\n" + hasil_penulisan + "\n" + "================================" + "\n"  + hasil_baca)
