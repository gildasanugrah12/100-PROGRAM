def limassegiempat():
    print('='*40)
    print('\tRUMUS LIMAS SEGIEMPAT')
    print('='*40)

    a = int(input('MASUKAN ALAS\t\t\t: '))
    t = int(input('MASUKAN TINGGI\t\t\t: '))
    s = int(input('MASUKAN SISI \t\t\t: '))
    st = int(input('MASUKAN SISI TEGAK\t\t'))
    
    l = lambda a,t,s,st: a + st
    vol = lambda a,t,s,st: 1/3 * a * t *s

    print("LUAS \t\t:", l(a,t,s,st))
    print("VOLUME \t\t:",vol(a,t,s,st))
          
limassegiempat()