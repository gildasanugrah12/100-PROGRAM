def layang_layang():
    print('='*40)
    print('\tRUMUS LAYANG LAYANG')
    print('-'*40)

    d1 = int(input("MASUKAN DIAGONAL 1\t\t: "))
    d2 = int(input("MASUKAN DIAGONAL 2\t\t: "))
    a = int(input("MASUKAN SISI A\t\t\t: "))
    b = int(input("MASUKAN SISI B\t\t\t: "))

    L = lambda diagonal1,diagonal2,a,b: d1 * d2
    K = lambda diagonal1,diagonal2,a,b: 2 * ( a + b )

    print("LUAS LAYANG LAYANG\t\t:", L(d1,d2,a,b), 'Cm2')
    print("KELILING LAYANG LAYANG\t\t:", K(d1,d2,a,b), 'Cm2')

layang_layang()