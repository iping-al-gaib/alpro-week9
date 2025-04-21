from greeting import greeting
from menu import tampilkan_menu, ambil_harga
from billing import generate_bill
from discount import calculate_discount
from inventory import show_inventory, cek_stok, inventory_data  # tambahan

def pesan_kopi():
    nama = input("Masukkan nama Anda: ")
    
    # Sapa user
    greeting(nama)
    
    # Tampilkan stok
    show_inventory()
    
    # Tampilkan menu
    tampilkan_menu()
    
    # Input pilihan
    pilihan = input("\nSilakan pilih menu (1-4): ")
    menu, harga = ambil_harga(pilihan)

    if menu:
        try:
            jumlah = int(input("Masukkan jumlah pesanan: "))
            if jumlah <= 0:
                print("❌ Jumlah harus lebih dari 0.")
                return
        except ValueError:
            print("❌ Input jumlah tidak valid.")
            return

        # ❗️Cek apakah stok mencukupi
        if not cek_stok(menu, jumlah):
            print(f"❌ Maaf, stok tidak mencukupi. Hanya tersedia {inventory_data.get(menu, 0)}.")
            return

        # Diskon?
        diskon = input("Apakah Anda punya kupon diskon? (y/n): ")
        if diskon.lower() == "y":
            harga = calculate_discount(harga, 10)
            print("✅ Diskon 10% diterapkan!")

        # Cetak tagihan
        generate_bill(nama, menu, harga, jumlah)
    else:
        print("❌ Maaf, pilihan tidak valid.")

# Jalankan program
pesan_kopi()
