# Write code below 💖


def get_item(nomor):
    if nomor == 1:
        return "🍔 Cheeseburger"
    elif nomor == 2:
        return "🍟 Fries"
    elif nomor == 3:
        return "🥤 Soda"
    elif nomor == 4:
        return "🍦 Ice Cream"
    elif nomor == 5:
        return "🍪 Cookie"
    else:
        return "Item tidak ditemukan!"


def welcome():
    print("=================================")
    print("🍽️  Selamat Datang di Aizayn Café!")
    print("=================================")
    print("Menu yang tersedia:")
    print("1. 🍔 Cheeseburger")
    print("2. 🍟 Fries")
    print("3. 🥤 Soda")
    print("4. 🍦 Ice Cream")
    print("5. 🍪 Cookie")
    print("=================================")


welcome()

pilih = int(input("Masukkan Nomor Item pesanan yang ingin anda pesan (1-5): "))

order = get_item(pilih)

print(f"\nAnda Memesan : {order}")
