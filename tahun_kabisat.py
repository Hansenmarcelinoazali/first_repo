year = int(input("masukan tahun: ")) #input angka (tahun) yang di inginkan
#tahun kabisat adalah tahun dimana februari mempunyai tanggal 29 dan terjadi 4 tahun sekali

# Leap Year Check
if year % 4 == 0 and year % 100 != 0: #jika tahun yang di input modul0==4 dan hasilnya 0 maka tahun  tersebut adalah tahun kabisat
    print(year, "Tahun Kabisat")
elif year % 100 == 0: #jika tahun tersebut di modulo dengan 100 dan hasillnya 0 maka tidak masuk dalam tahun kabisat
    print(year, "Bukan Tahun Kabisat")
elif year % 400 ==0: #jika tahun tersebut dibagi dengan 4 dan hasilnya 0 maka tahun tersebut adalah tahun kabisat
    print(year, "Tahun Kabisat")
else:
    print(year, "bukan tahun kabisat") #selain dari itu adalah bukan tahun kabisat