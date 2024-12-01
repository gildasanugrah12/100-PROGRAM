def konversi_waktu_ke_detik():
    jam = int(input("Masukkan jam: "))
    menit = int(input("Masukkan menit: "))
    detik = int(input("Masukkan detik: "))
    
    total_detik = (jam * 3600) + (menit * 60) + detik
    print(f"{jam} jam, {menit} menit, {detik} detik = {total_detik} detik")

konversi_waktu_ke_detik()
