def belahketupat():
    print('='*30)
    print('\tRUMUS BELAH KETUPAT')
    print('='*30)

    d1 = int(input('MASUKAN DIAGONAL 1\t: '))
    d2 = int(input('MASUKAN DIAGONAL 2\t: '))
    s = int(input('MASUKAN SISI\t\t: '))
    
    l = lambda d1,d2,s: 1/2 * d1 * d2
    kel = lambda d1,d2,s: 4 * s

    print('LUAS \t\t\t:', l(d1,d2,s))
    print('KELILING \t\t:',kel(d1,d2,s))

belahketupat()


