import datetime
print("Kalkulator Tahun Lahir")
nama = input("Siapa nama kamu: ")
umur = input("Berapa Usia kamu: ")
waktu = datetime.datetime.now()
tahunini = waktu.year
usia = int(tahunini) - int(umur)

print ("Halo",nama,", Kamu lahir pada tahun:", usia)