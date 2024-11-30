statusLampu = input("Status Lampu : ").lower()
warnalampu = input("Masukan warna lampu : ").lower()

if statusLampu =='menyala':
    if warnalampu == 'merah':
        print('Berhenti')
    elif warnalampu == 'kuning':
        print('Bersiap')
    elif warnalampu == 'hijau':
        print('Maju')
    else:
        print('Tidak Ada Warna')
else:
    print('Trobos')