def nilai_tertinggi():
    arr = [int(x) for x in input("Masukkan angka-angka, pisahkan dengan spasi: ").split()]
    print(f"Nilai tertinggi adalah: {max(arr)}")

nilai_tertinggi()
