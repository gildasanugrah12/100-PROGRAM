print('-'*40)
print('\t\tDISKON')
print('-'*40)

def hitung_diskon(total_belanja):
    if total_belanja > 100000:
        diskon = total_belanja * 0.10
    else:
        diskon = 0

    total_setelah_diskon = total_belanja - diskon

    return diskon, total_setelah_diskon

total_belanja = float(input("Masukan nilai total belanja: Rp"))
diskon, total_setelah_diskon = hitung_diskon(total_belanja)

print(f"Diskon yang diberikan: Rp{diskon:.2f}")
print(f"Nilai belanja setelah dikurangi diskon: Rp{total_setelah_diskon:.2f}")