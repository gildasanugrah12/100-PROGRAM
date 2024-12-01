def ke_romawi(angka):
    romawi = {
        1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 
        90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"
    }
    
    hasil = ""
    for nilai in sorted(romawi.keys(), reverse=True):
        while angka >= nilai:
            hasil += romawi[nilai]
            angka -= nilai
    
    return hasil

angka = int(input("Masukkan angka untuk dikonversi ke angka Romawi: "))
print(f"Angka {angka} dalam angka Romawi adalah {ke_romawi(angka)}")
