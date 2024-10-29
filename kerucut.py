print ("="*25)
print ("\tkerucut")
print ("="*25)

PHI = 3.14
s = int(input('masukan nilai sisi\t: '))
t = int(input('masukan nilai tinggi\t: '))
r = int(input('masukan nilai jari jari alas kerucut\t: '))

ls = PHI * r * s
lp = (PHI * r * s) + (PHI * r ** 2)
v = 1/3 * PHI * r **2 * t

print ('LUAS KERUCUT\t\t:',ls)
print ('LUAS PERMUKAAN\t\t:',lp)
print ('VOLUME\t\t\t:',v)

