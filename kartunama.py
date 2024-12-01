from pdb import Image, ImageDraw, ImageFont

def buat_kartu_nama():
    # Informasi yang diminta dari pengguna
    nama = input("Masukkan nama: ")
    jabatan = input("Masukkan jabatan: ")
    alamat = input("Masukkan alamat: ")
    telepon = input("Masukkan nomor telepon: ")
    
    # Ukuran gambar kartu nama (lebar, tinggi)
    lebar = 400
    tinggi = 250
    
    # Membuat gambar baru dengan latar belakang putih
    gambar = Image.new("RGB", (lebar, tinggi), "white")
    draw = ImageDraw.Draw(gambar)
    
    # Menggunakan font default
    font = ImageFont.load_default()
    
    # Menggambar judul kartu nama
    draw.text((150, 20), "Kartu Nama", fill="black", font=font)
    
    # Menambahkan informasi
    draw.text((20, 60), f"Nama     : {nama}", fill="black", font=font)
    draw.text((20, 90), f"Jabatan  : {jabatan}", fill="black", font=font)
    draw.text((20, 120), f"Alamat   : {alamat}", fill="black", font=font)
    draw.text((20, 150), f"Telepon  : {telepon}", fill="black", font=font)
    
    # Menyimpan gambar sebagai file
    gambar.save("kartu_nama.png")
    
    # Menampilkan gambar
    gambar.show()

# Memanggil fungsi untuk membuat kartu nama
buat_kartu_nama()
