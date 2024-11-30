nilaiKarakter = input("MASUKAN NILAI KARAKTER\t: ")
nilaiMTK = int(input("MASUKAN NILAI MTK\t: "))
nilaiINDO = int(input("MASUKAN NILAI B.INDO\t: "))
nilaiINGGRIS = int(input("MASUKAN NILAI B.INGGRIS\t: "))

if nilaiKarakter == "a" or nilaiKarakter == "b" and nilaiMTK >= 60 and nilaiINDO >= 70 and nilaiINGGRIS >= 55:
    print("kamu lulus")
else:
    print("kamu tidak lulus")