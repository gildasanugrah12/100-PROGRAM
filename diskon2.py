totalharga = float(input('MASUKAN HARGA BARANG\t: Rp. '))
diskon = 0

if totalharga >= 100000:
    diskon = (2/100) * totalharga
elif totalharga >= 500000:
    diskon = (4/100) * totalharga
elif totalharga >= 1000000:
    diskon = (6/100) * totalharga

totalbayar = totalharga - diskon

print(f'''
Harga Beli  : {totalharga}
Diskon      : {diskon}
Dibayar     : {totalbayar}
''')