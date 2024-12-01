from datetime import datetime

def cek_tanggal_valid():
    tanggal_input = input("Masukkan tanggal (format: dd-mm-yyyy): ")

    try:
        tanggal = datetime.strptime(tanggal_input, "%d-%m-%Y")
        print("Tanggal valid:", tanggal.strftime("%d-%m-%Y"))
    except ValueError:
        print("Tanggal tidak valid. Pastikan formatnya benar dan tanggal tersebut ada.")

cek_tanggal_valid()
