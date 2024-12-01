import calendar

def tampilkan_kalender():
    tahun = int(input("Masukkan tahun: "))
    bulan = int(input("Masukkan bulan: "))
    print(calendar.month(tahun, bulan))

tampilkan_kalender()
