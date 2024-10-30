# Program Kalkulator Sederhana 
Program ini adalah kalkulator sederhana yang memungkinkan pengguna untuk melakukan operasi 
aritmatika dasar: penjumlahan, pengurangan, perkalian, dan pembagian. Program ini ditulis dalam Python 
dan menggunakan input dari pengguna untuk mendapatkan angka dan jenis operasi yang diinginkan.

# Deskripsi Program
program ini dibuat menggunakan bahasa python dengan fitur : 

- Memungkinkan pengguna untuk memasukkan dua angka.
- Mendukung empat operasi aritmatika:
- Penjumlahan (+)
- Pengurangan (-)
- Perkalian (*)
- Pembagian (/)
- Menangani pembagian dengan nol dengan pesan kesalahan yang sesuai.
- Menawarkan opsi untuk melakukan perhitungan baru setelah hasil ditampilkan.

# Flowchart Program 
![Flowchart](https://github.com/vivitnh23/Lab2py/blob/main/flowchartkalkulator.png?raw=true)

  # Kode Program
```python
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("Pilih operasi aritmatika:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")
operator = input("Masukkan pilihan operasi (+, -, *, /): ")

if operator == '+':
    hasil = angka1 + angka2
    print("Hasil dari penjumlahan:", hasil)
elif operator == '-':
    hasil = angka1 - angka2
    print("Hasil dari pengurangan:", hasil)
elif operator == '*':
    hasil = angka1 * angka2
    print("Hasil dari perkalian:", hasil)
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
        print("Hasil dari pembagian:", hasil)
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
else:
    print("Operator tidak valid. Silakan pilih (+, -, *, /).")
```
# Output Program
````
Masukkan angka pertama: 8000
Masukkan angka kedua: 5600
Pilih operasi aritmatika:
1. Penjumlahan (+)
2. Pengurangan (-)
3. Perkalian (*)
4. Pembagian (/)
Masukkan pilihan operasi (+, -, *, /): +
Hasil dari penjumlahan: 13600.0
````
# Cara Kerja
Pengguna memasukkan 10 dan 5.
Pengguna memilih operator +.
Program menghitung 10 + 5 dan menampilkan hasil 15.0.
Program menanyakan apakah pengguna ingin melakukan perhitungan lagi.
Jika pengguna memilih 'y', proses dimulai lagi; jika 'n', program berhenti.
````


