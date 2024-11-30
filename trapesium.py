def trapesium():
    print('='*30 )
    print('\tRUMUS TRAPESIUM')
    print('-'*30)

    T = int(input("MASUKAN TINGGI TRAPESIUM\t: "))
    a = int(input("MASUKAN A\t\t\t: "))
    b = int(input("MASUKAN B\t\t\t: "))
    c = int(input("MASUKAN C\t\t\t: "))
    d = int(input("MASUKAN D\t\t\t: "))

    L = lambda T,a,b,c,d: 1/2 * ( a + b ) * T
    K = lambda T,a,b,c,d: a + b + c + d

    print("LUAS TRAPESIUM\t\t\t:", L(T,a,b,c,d), 'Cm2')
    print("kELILING TRAPESIUM\t\t:", K(T,a,b,c,d), 'Cm2')

trapesium()