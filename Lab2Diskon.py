harga_reguler = 50000
harga_vip = 100000

tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").lower()

status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

if tipe_tiket == "reguler":
    harga_tiket = harga_reguler
elif tipe_tiket == "vip":
    harga_tiket = harga_vip
else:
    print("Tipe tiket tidak valid.")
    exit()

if status_member == "ya":
    total_harga = harga_tiket * 0.8  # Diskon 20%
else:
    total_harga = harga_tiket

print("Total harga yang harus dibayar: Rp", int(total_harga))