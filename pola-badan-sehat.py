berat_badan = float(input("Masukkan berat badan Anda (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan Anda (cm): "))
    
bmi = berat_badan / ((tinggi_badan / 100) ** 2)
    
if bmi < 18.5:
    print("Kekurangan berat badan.")
elif 18.5 <= bmi < 24.9:
    print("Berat badan ideal.")
else:
    print("Kelebihan berat badan.")