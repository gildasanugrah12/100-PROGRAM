berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (cm): ")) / 100

bmi = berat / (tinggi ** 2)

print(f"Indeks Massa Tubuh (BMI) Anda adalah: {bmi:.2f}")