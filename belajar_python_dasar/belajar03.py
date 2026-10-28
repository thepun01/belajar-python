# Materi: if/elif/else
# Studi Kasus: Program cek predikat nilai
print("================================")
print("Program Cek Predikat Nilai")
print("================================")

# input
input_nilai = int(input("Masukan Nilai Rata-Rata Anda (0-100): "))

# proses
if input_nilai >= 90 and input_nilai <= 100:
    
    # output
    print("Predikat Nilai Anda: A")
    
elif input_nilai >= 80 and input_nilai < 90:
    
    # output
    print("Predikat Nilai Anda: B")
    
elif input_nilai >= 70 and input_nilai < 80:
    
    # output
    print("Predikat Nilai Anda: C")
    
elif input_nilai >= 60 and input_nilai < 70:
    
    # output
    print("Predikat Nilai Anda: D")
    
elif input_nilai >= 50 and input_nilai < 60:
    
    # output
    print("Predikat Nilai Anda: E")
    
elif input_nilai < 50 and input_nilai >= 0:
    
    # output
    print("Predikat Nilai Anda: F")
    
else:
    # output
    print("Nilai yang Anda masukan tidak valid, silahkan masukan nilai antara 0-100")

print("================================")