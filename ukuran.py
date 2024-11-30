sepatu = int(input('Masukan ukuran\t: '))

if sepatu > 30 and sepatu <= 35:
    print("KECIL")
elif sepatu > 35 and sepatu <= 40:
    print("SEDANG")
elif sepatu > 40 and sepatu <= 46:
    print("BESAR")
else:
    print("Ukuran yang di masukan salah")