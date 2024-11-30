print('-'*40)
print('\t\tKALKULATOR')
print('-'*40)

def kalkulator_sederhana():
    try:
        operand1 = float(input("Masukan operand 1 \t\t: "))
        operator = input("Masukan operator (+, -, *, /) \t: ")
        operand2 = float(input("Masukan operand 2 \t\t: "))

        if operator == '+':
            hasil = operand1 + operand2
        elif operator == '-':
            hasil = operand1 - operand2
        elif operator == '*':
            hasil = operand1 * operand2
        elif operator == '/':
            hasil = operand1 / operand2
        else:
            print("Tidak ada angka ini")

            return
        
        print(f"Hasil hitung: {hasil}")
    except ValueError:
        print("Tidak ada angka ini")

        return
    
kalkulator_sederhana()
