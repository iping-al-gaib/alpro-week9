def tampilkan_menu():
    print("\n=== MENU KAFE KOPI ===")
    print("1. Espresso            - Rp 18000")
    print("2. Cappuccino          - Rp 25000")
    print("3. Latte               - Rp 22000")
    print("4. Caramel Macchiato   - Rp 30000")

def ambil_harga(pilihan):
    if pilihan == "1":
        return "Espresso", 18000
    elif pilihan == "2":
        return "Cappuccino", 25000
    elif pilihan == "3":
        return "Latte", 22000
    elif pilihan == "4":
        return "Caramel Macchiato", 30000
    else:
        return None, 0
