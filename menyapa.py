from datetime import datetime

jam_sekarang = datetime.now().hour

if jam_sekarang < 12:
    sapaan = "Selamat Pagi!"
elif jam_sekarang < 18:
    sapaan = "Selamat Siang!"
else:
    sapaan = "Selamat Malam!"

print(sapaan)