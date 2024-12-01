def konversi_mata_uang():
    usd = float(input("Masukkan jumlah USD: "))
    kurs = 14500  
    idr = usd * kurs
    print(f"{usd} USD = {idr} IDR")

konversi_mata_uang()
