import random

def angka_acak():
    batas_bawah = int(input("Masukkan batas bawah: "))
    batas_atas = int(input("Masukkan batas atas: "))

    angka = random.randint(batas_bawah, batas_atas)
    
    print(f"Angka acak antara {batas_bawah} dan {batas_atas}: {angka}")

angka_acak()
