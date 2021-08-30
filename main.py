
# import datetime
# print("Kalkulator Tahun Lahir")
# nama = raw_input("Siapa nama kamu: ")
# umur = input("Berapa Usia kamu: ")
# waktu = datetime.datetime.now()
# tahunini = waktu.year
# usia = tahunini - umur
#
# print "Halo",nama,", Kamu lahir pada tahun:", usia
#print waktu
print("Kalkulator Sangat Amat Sederhana")
kumpulanoperator = ["+", "-", "x", "/"]
var1 = input("Angka pertama: ")
operan = input("Tambah (+), Kurang (-), Kali (x), Bagi (/): ")
var2 = input("Angka kedua: ")
hasiljumlah = int(var1) + int(var2)
hasilkurang = int(var1) - int(var2)
hasilkali = int(var1) * int(var2)
hasilbagi = int(var1) / int(var2)
if (operan == "+"):
    print (hasiljumlah)
elif (operan == "-"):
    print (hasilkurang)
elif (operan == "x"):
    print (hasilkali)
elif (operan == "/"):
    print (hasilbagi)
else:
    print("Salah Operator ")
lanjut = input("Apakah ingin mengulangi (Y/T): ")
if (lanjut == "T"):
    quit()


