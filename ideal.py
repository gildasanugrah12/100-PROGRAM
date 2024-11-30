print('-'*40)
print('\t\tIDEAL')
print('-'*40)

berat_badan = float(input("Masukan berat badan (kg):  "))
tinggi_badan_cm = float(input("Masukan tinggi badan (cm): "))
jenis_kelamin = input("Masukan jenis kelamin (L/P): ")

if jenis_kelamin == 'L':
    berat_badan_ideal = tinggi_badan_cm - 100
elif jenis_kelamin == 'P':
    berat_badan_ideal = tinggi_badan_cm - 105
else:
    print("Jenis kelamin tidak valid. Gunakan 'L' untuk laki-laki dan 'P' untuk perempuan.")

batas_bawah = berat_badan_ideal -2
batas_atas = berat_badan_ideal + 2

if batas_bawah <= berat_badan <= batas_atas:
    print("Ideal")
else:
    print("Tidak ideal")