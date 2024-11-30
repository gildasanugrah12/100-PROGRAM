size = int(input('Ukuran sepatu: '))

if size > 40 and size < 46:
    print('Your shoes is big')
elif size > 35 and size < 40:
    print('Your shoes is medium')
elif size > 30 and size < 35:   
    print('Your shoes is small')
else:
    print('size is wrong')