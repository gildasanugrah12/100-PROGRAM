def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def volume_limas_segita(alas, tinggi_segitiga, tinggi_limas):
    luas_alas = luas_segitiga(alas, tinggi_segitiga)
    return (1/3) * luas_alas * tinggi_limas

alas = float(input("Masukkan panjang alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
tinggi_limas = float(input("Masukkan tinggi limas: "))
volume = volume_limas_segita(alas, tinggi_segitiga, tinggi_limas)

print(f"Volume limas segitiga adalah: {volume:.2f}")