def tabung():
    print("="*30)
    print("\tRUMUS TABUNG")
    print("-"*30)

    PHI = 3.14
    r = int(input('MASUKAN JARI JARI\t: '))
    t = int(input('MASUKAN TINGGI\t\t: '))

    ls = lambda r,t: 2 * PHI * r * t
    lp = lambda r,t: 2 * PHI * r * t + 2 * PHI * r**2
    v = lambda r,t: PHI * r**2 * t

    print("LUAS SELIMUT\t\t:", ls(r,t))
    print("LUAS PERMUKAAN\t\t:", lp(r,t))
    print("VOLUME\t\t\t:", v(r,t))

tabung()