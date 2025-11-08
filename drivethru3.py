# 🍽️ Codédex Café — Multi Menu Order System
# Tujuan: Memesan lebih dari 1 menu, menampilkan harga per item, dan menghitung total harga.


# ================================================================
# 1️⃣ Daftar Menu dan Harga
# ---------------------------------------------------------------
# Kita simpan menu dan harga dalam dictionary agar mudah diakses.
# Key = nomor menu, Value = tuple berisi (nama item, harga)
# ================================================================
menu_items = {
    1: ("🍔 Cheeseburger", 35000),
    2: ("🍟 Fries", 15000),
    3: ("🥤 Soda", 10000),
    4: ("🍦 Ice Cream", 20000),
    5: ("🍪 Cookie", 12000),
}


# ================================================================
# 2️⃣ Fungsi get_item()
# ---------------------------------------------------------------
# Menerima 1 parameter (nomor menu)
# Mengembalikan nama item dan harga dalam bentuk tuple
# ================================================================
def get_item(number):
    if number in menu_items:
        return menu_items[number]  # return (nama, harga)
    else:
        return ("❌ Item tidak ditemukan!", 0)


# ================================================================
# 3️⃣ Fungsi welcome()
# ---------------------------------------------------------------
# Menampilkan daftar menu dan harga
# ================================================================
def welcome():
    print("===================================")
    print("🍽️  Selamat Datang di Codédex Café!")
    print("===================================")
    print("Menu yang tersedia:")
    for num, (item, price) in menu_items.items():
        print(f"{num}. {item:<15} Rp{price:,}")
    print("===================================")


# ================================================================
# 4️⃣ Program Utama
# ---------------------------------------------------------------
# Langkah:
#   1. Tampilkan menu
#   2. Minta user memilih beberapa item (pisahkan dengan koma)
#   3. Tampilkan daftar pesanan + total harga
# ================================================================
def main():
    welcome()

    # Minta input dari user, misalnya: "1,3,5"
    pilihan = input(
        "Masukkan nomor menu yang ingin Anda pesan (pisahkan dengan koma): "
    )

    # Pisahkan input berdasarkan koma, lalu ubah menjadi integer
    pilihan_list = [int(x.strip()) for x in pilihan.split(",")]

    # Variabel untuk menyimpan total harga
    total_harga = 0

    print("\n🧾 Pesanan Anda:")
    print("-------------------------------")

    # Loop setiap pilihan menu
    for nomor in pilihan_list:
        item, harga = get_item(nomor)  # panggil fungsi get_item()
        print(f"{item:<15} Rp{harga:,}")
        total_harga += harga

    print("-------------------------------")
    print(f"💰 Total Harga: Rp{total_harga:,}")
    print("Terima kasih sudah memesan di Codédex Café! 🙌")


# ================================================================
# 5️⃣ Jalankan Program
# ================================================================
main()
