def kartu_angka():
    baris = int(input("Masukkan jumlah baris kartu: "))
    kolom = int(input("Masukkan jumlah kolom kartu: "))
    
    angka = 1
    for i in range(baris):
        for j in range(kolom):
            print(f"| {angka:2} ", end="")
            angka += 1
        print("|")  

kartu_angka()
