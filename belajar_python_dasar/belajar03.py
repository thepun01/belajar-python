# Materi: if/elif/else
# Studi Kasus: Program cek predikat nilai
print("================================")
print("Program Cek Predikat Nilai")
print("================================")
input_nilai = int(input("Masukan Nilai Rata-Rata Anda (0-100): "))

if input_nilai >= 90 and input_nilai <= 100:
    print("Predikat Nilai Anda: A")
elif input_nilai >= 80 and input_nilai < 90:
    print("Predikat Nilai Anda: B")
elif input_nilai >= 70 and input_nilai < 80:
    print("Predikat Nilai Anda: C")
elif input_nilai >= 60 and input_nilai < 70:
    print("Predikat Nilai Anda: D")
elif input_nilai >= 50 and input_nilai < 60:
    print("Predikat Nilai Anda: E")
elif input_nilai < 50 and input_nilai >= 0:
    print("Predikat Nilai Anda: F")
else:
    print("Nilai yang Anda masukan tidak valid, silahkan masukan nilai antara 0-100")

print("================================")