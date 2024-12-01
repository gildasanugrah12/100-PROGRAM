def kata_terpanjang(kalimat):
    kata = kalimat.split()
    panjang = max(kata, key=len)
    print(f"Kata terpanjang adalah: {panjang}")

kalimat = input("Masukkan kalimat: ")
kata_terpanjang(kalimat)
