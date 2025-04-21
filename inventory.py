inventory_data = {
    "Espresso": 15,
    "Cappuccino": 10,
    "Latte": 20,
    "Caramel Macchiato": 8
}

def show_inventory():
    print("\n📦 Stok hari ini:")
    for item, stok in inventory_data.items():
        print(f"- {item}: {stok} cups")

def cek_stok(menu, jumlah):
    return inventory_data.get(menu, 0) >= jumlah
