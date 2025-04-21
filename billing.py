def generate_bill(menu, harga, jumlah):
    total = harga * jumlah
    print(f"\nPesanan kamu adalah: {menu} (x{jumlah})")
    print(f"Total yang harus dibayar: Rp {total}")
    print(f"Jumlah item dipesan: {jumlah}")
    print("Silakan tunggu, pesananmu sedang disiapkan...")
