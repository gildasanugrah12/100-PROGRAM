huruf = input("Masukan sebuah huruf: ")

huruf = huruf.upper()

if huruf.isalpha() and len(huruf) == 1:
    if huruf in ['A','E','I','O','U']:
        print(f"{huruf} adalah huruf vokal.")
    else:
        print(f"{huruf} adalah huruf konsonan.")
else:
    print(f"{huruf} bukan berupa huruf.")
