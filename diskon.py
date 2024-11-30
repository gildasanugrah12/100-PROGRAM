print('*'*48)
jumlah = int(input("Masukan total harga : "))
print("*"*48)

diskon = 0
if jumlah >= 100000:
    diskon = 0.05 * jumlah
    total_harga = jumlah - diskon
    print("Diskon yang di dapat :", diskon)
    print("Total harga yang harus di bayar : ", total_harga)
elif jumlah <= 100000:
    print ("Total harga : ", jumlah)