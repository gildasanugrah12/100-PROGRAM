def persegi_panjang():
    print('='*40)
    print('\tRUMUS PERSEGI PANJANG')
    print('='*40)

    P = int(input('MASUKAN PANJANG\t\t\t: '))
    L = int(input('MASUKAN LEBAR\t\t\t: '))

    l = lambda P,L: P * L
    K = lambda P,L: 2 * (P + L)

    print('LUAS PERSEGI PANJANG\t\t:', l(P,L), 'Cm2')
    print('KELILING PERSEGI PANJANG\t:', K(P,L), 'Cm2')

persegi_panjang()
