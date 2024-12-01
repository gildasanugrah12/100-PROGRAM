from PIL import Image, ImageDraw, ImageFont

def buat_kartu_nama():
    nama = input("Masukkan nama: ")
    jabatan = input("Masukkan jabatan: ")
    alamat = input("Masukkan alamat: ")
    telepon = input("Masukkan nomor telepon: ")
    
    lebar = 400
    tinggi = 250
    
    gambar = Image.new("RGB", (lebar, tinggi), "white")
    draw = ImageDraw.Draw(gambar)
    
    font = ImageFont.load_default()
    
    draw.text((150, 20), "Kartu Nama", fill="black", font=font)

    draw.text((20, 60), f"Nama     : {nama}", fill="black", font=font)
    draw.text((20, 90), f"Jabatan  : {jabatan}", fill="black", font=font)
    draw.text((20, 120), f"Alamat   : {alamat}", fill="black", font=font)
    draw.text((20, 150), f"Telepon  : {telepon}", fill="black", font=font)
    
    gambar.save("kartu_nama.png")

    gambar.show()

buat_kartu_nama()
