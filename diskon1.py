harga = int(input('MASUKAN HARGA BARANG\t: Rp. '))

if harga >= 100000:
    diskon = (50/100) * harga
    harga = harga - diskon


print('DISKON\t\t\t: Rp.',diskon)
print('TOTAL YANG DI BAYAR\t: Rp.' ,harga)