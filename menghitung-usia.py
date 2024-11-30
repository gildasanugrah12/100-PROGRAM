from datetime import datetime

def hitung_usia(tanggal_lahir):

    tanggal_lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d")
    
    hari_ini = datetime.today()
    
    usia = hari_ini.year - tanggal_lahir.year
    
    if hari_ini.month < tanggal_lahir.month or (hari_ini.month == tanggal_lahir.month and hari_ini.day < tanggal_lahir.day):
        usia -= 1
    
    return usia

tanggal_lahir = "2000-05-15"  
usia = hitung_usia(tanggal_lahir)
print(f"Usia Anda adalah {usia} tahun.")