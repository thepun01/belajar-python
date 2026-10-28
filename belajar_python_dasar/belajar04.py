# Materi: for dan while
# Studi Kasus: Program Mencetak Tabel Perkalian
print("================================")
print("Program Mencetak Tabel Perkalian")
print("================================")

# input
input_angka = int(input("Masukan Angka: "))

# keterangan
print(f"Berikut Tabel Perkalian dari Angka {input_angka}: ")

# proses
for i in range(1, 11):
    # output
    print(f"{input_angka} x {i} = {input_angka * i}")

print("================================")