print('-'*50)
print('\t\t BILANGAN BULAT')
print('-'*50)


a = int(input("MASUKAN BILANGAN 1\t: "))
b = int(input("MASUKAN BILANGAN 2\t: "))
c = int(input("MASUKAN BILANGAN 3\t: "))

if a>b:
    a,b=b,a
if b>c:
    b,c=c,b
if a>b:
    a,b=b,a

print("BILANGAN KECIL KE BESAR\t: ",a,b,c)