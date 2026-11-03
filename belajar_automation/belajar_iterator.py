list_angka = [10,20,30,40,50] # ini adalah tipe data list
iterator_angka = iter(list_angka) # ini adalah tipe data iterator

print(type(list_angka))
print(type(iterator_angka))
print("================================")

print(list_angka)

print(iterator_angka) 
# mengakses iterator di atas tidak bisa seperti ini, harus menggunakan fungsi next() atau diubah menjadi list 

print("================================")

# mengakses iterator menggunakan fungsi next()
print(next(iterator_angka)) # mengakses iterator menggunakan fungsi next()
print(next(iterator_angka))
print(next(iterator_angka))

# print(list(iterator_angka)) # mengubah iterator menjadi list

list_angka.append(60) # menambahkan data ke list_angka
# print(list_angka)

print(next(iterator_angka))
print(next(iterator_angka))
print(next(iterator_angka))

# Dari contoh di atas, iterator memiliki sifat
# 1. Hanya bisa diakses satu kali
# 2. Ketika sudah diakses, tidak bisa diakses lagi atau bisa habis (exhausted)
# 3. Iterator tidak membuat salinan list, sehingga jika list diubah, iterator juga akan berubah


