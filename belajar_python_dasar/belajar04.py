# Materi: for dan while
# Studi Kasus: Program Mencetak Tabel Perkalian
print("================================")
print("Program Mencetak Tabel Perkalian")
print("================================")
input_angka = int(input("Masukan Angka: "))
print(f"Berikut Tabel Perkalian dari Angka {input_angka}: ")
for i in range(1, 11):
    print(f"{input_angka} x {i} = {input_angka * i}")
print("================================")