angka = int(input("angka : "))
angka_2 = int(input("angka : "))
soal = input("+, -, /, * : ") 

if soal == '+' :
    hasil = int(angka+angka_2)
    print (hasil)

elif soal == '-' :
    hasil = int(angka-angka_2)
    print (hasil)

elif soal == '*' :
    hasil = int(angka*angka_2)
    print (hasil)

elif soal == '/' :
    hasil = int(angka/angka_2)
    print (hasil)