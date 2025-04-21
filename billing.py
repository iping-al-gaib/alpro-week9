def generate_bill(nama, menu, harga, jumlah):
    total = harga * jumlah
    print(f"\nHALOO!!, {nama}!")
    print(f"Pesanan kamu adalah: {menu} (x{jumlah})")
    print(f"Total yang harus dibayar: Rp {total}")
    print("Silakan ditunggu ya, pesananmu sedang dibuatkan...")
