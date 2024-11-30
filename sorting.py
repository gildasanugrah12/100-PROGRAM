a = int(input("Masukan Nilai A: "))
b = int(input("Masukan Nilai B: "))
c = int(input("Masukan Nilai C: "))

if a > b and a > c:
    print("Angka terbesar adalah:", a)
    if b < c:
        print("Angka ditengah adalah:", c)
        print("Angka terkecil adalah:", b)
    elif c < b:
        print("Angka ditengah adalah:", b)
        print("Angka terkecil adalah:", c)
elif b > a and b > c:
    print("Angka terbesar adalah:", b)
    if a < c:
        print("Angka ditengah adalah:", c)
        print("Angka terkecil adalah:", a)
    elif c < a:
        print("Angka ditengah adalah:", a)
        print("Angka terkecil adalah:", c)
else:
    print("Angka terbesar adalah:", c)
    if a < b:
        print("Angka ditengah adalah:", b)
        print("Angka terkecil adalah:", a)
    elif b < a:
        print("Angka ditengah adalah:", a)
        print("Angka terkecil adalah:", b)