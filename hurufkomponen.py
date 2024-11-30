def cek_huruf(huruf):
    huruf = huruf.upper()
    if huruf.isalpha() and len(huruf) == 1:
        if huruf in 'AEIOU':
            return 'HURUF ADALAH VOKAL'
        else:
                return ' HURUF ADALAH KONSONAN'
    else:
        return 'BUKAN HURUF'

inputan_huruf = input('MASUKKAN SABUAH HURUF (A-Z):')
print(cek_huruf(inputan_huruf))