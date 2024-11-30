umur = int(input("Masukkan umur Anda : "))
    
if umur < 17:
    tidur = 12
elif umur <= 28:
    tidur = 8
else:
    tidur = 9
    
print(f"Jumlah jam tidur yang disarankan: {tidur} jam per malam.")