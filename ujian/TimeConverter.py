def seconds_to_dhms(time):
    seconds_to_minute   = 60 #1 menit adalah 60 detik
    seconds_to_hour     = 60 * seconds_to_minute #1 jam adalah 3600 detik
    seconds_to_day      = 24 * seconds_to_hour #1 hari sama dengan 86400 detik

    days    =   time // seconds_to_day #dari keterangan hari  dibagi dengan detik yang ada
    time    %=  seconds_to_day #jika waktu nya sama dengan dengan hari 

    hours   =   time // seconds_to_hour #waktu perdetik maka akan di bagi dengan waktu perjam 
    time    %=  seconds_to_hour #waktu yang sama dengan modulo atau dibagi

    minutes =   time // seconds_to_minute #waktu dalam 1 menit akan gibagi dengan waktu permenit
    time    %=  seconds_to_minute #waktu tersebut dimodulo dengan waktu permenit 

    seconds = time #waktu perdetik akan sama dengan waktu perdetik yang telah di input

    print("%d days, %d hours, %d minutes, %d seconds" % (days, hours, minutes, seconds)) #pemanggilan berdasarkan dengan day, hour, time


time = int(input("masukan detik yang di inginkan: "))
seconds_to_dhms(time)

#nama func saya ubah karna eror kalau pakai TImeConverter (gak tau knapa )saya biasa pake jupyter jadi saya ubah d=jadi dhms (day,hour,minutes,second)