import math

def kalkulator_lingkaran():
    jari_jari = float(input("Masukkan jari-jari lingkaran (dalam satuan panjang): "))
    
    luas = math.pi * jari_jari ** 2
    
    keliling = 2 * math.pi * jari_jari
    
    print(f"Luas lingkaran: {luas:.2f}")
    print(f"Keliling lingkaran: {keliling:.2f}")

kalkulator_lingkaran()
