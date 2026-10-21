# Materi: Baca Tulis File (File Handling)
# Studi Kasus: Programm Membaca dan Menulis File

# Read file
def read_file(file_path):
    try:
        file = open(file_path, "r")
        content = file.read()
        print("Isi File:")
        print(content)
        file.close()
    except FileNotFoundError:
        print(f"File '{file_path}' tidak ditemukan.")
        

def write_file(file_path, content):
    try:
        with open(file_path, "w") as file:
            file.write(content)
            print(f"Berhasil menulis ke file: {file_path}")
    except FileNotFoundError:
        print(f"File '{file_path}' tidak ditemukan.")

file_path = input("Masukkan path file yang ingin dibaca: ")
content_to_write = input("Masukkan isi file yang ingin ditulis: ")

write_file(file_path, content_to_write)
read_file(file_path)