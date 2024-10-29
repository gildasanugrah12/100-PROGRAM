print('*'*48)
print('\t\tPROGRAM TABUNG')
print("*"*48)

r = int(input('masukan nilai jari-jari\t:'))
tinggi = int(input('masukan nilai tinggi\t:'))

volume = 3.14 * r * r * tinggi
lp = 2 * 3.14
AA = r + tinggi 

print('Volume\t\t:',volume,'cm2')
print('Luas Permukaan\t\t:' ,lp * AA, 'cm2')