# 🔢 Interactive Calculator (Loop Version)
# Sekarang kalkulator bisa digunakan berkali-kali sampai user memilih keluar.

# ====================================================
# 🧮 1️⃣ Definisi Fungsi Matematika
# ====================================================

def add(a, b):
    # Fungsi untuk penjumlahan
    return a + b

def subtract(a, b):
    # Fungsi untuk pengurangan
    return a - b

def multiply(a, b):
    # Fungsi untuk perkalian
    return a * b

def divide(a, b):
    # Fungsi untuk pembagian
    # Tambahkan perlindungan agar tidak membagi dengan nol
    if b == 0:
        return "❌ Tidak bisa membagi dengan nol!"
    return a / b

def exp(a, b):
    # Fungsi untuk pangkat (a^b)
    return a ** b


# ====================================================
# 🧠 2️⃣ Program Utama (Loop)
# ====================================================

print("=== Kalkulator Python Interaktif ===")

# Gunakan while True untuk membuat program berjalan terus
while True:
    print("\nPilih operasi yang ingin dilakukan:")
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")
    print("5. Pangkat (**)")
    print("0. Keluar")

    # Ambil input pilihan dari user
    pilihan = input("Masukkan pilihan (0-5): ")

    # Jika user ingin keluar
    if pilihan == "0":
        print("\n👋 Terima kasih telah menggunakan kalkulator ini!")
        break  # menghentikan loop (keluar dari program)

    # Ambil dua angka dari user
    # Gunakan try-except agar tidak error jika user salah input
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("⚠️ Input tidak valid! Harap masukkan angka.")
        continue  # kembali ke awal loop

    # Gunakan if/elif/else untuk menentukan operasi
    if pilihan == "1":
        hasil = add(angka1, angka2)
        print(f"Hasil: {angka1} + {angka2} = {hasil}")

    elif pilihan == "2":
        hasil = subtract(angka1, angka2)
        print(f"Hasil: {angka1} - {angka2} = {hasil}")

    elif pilihan == "3":
        hasil = multiply(angka1, angka2)
        print(f"Hasil: {angka1} × {angka2} = {hasil}")

    elif pilihan == "4":
        hasil = divide(angka1, angka2)
        print(f"Hasil: {angka1} ÷ {angka2} = {hasil}")

    elif pilihan == "5":
        hasil = exp(angka1, angka2)
        print(f"Hasil: {angka1} ^ {angka2} = {hasil}")

    else:
        # Jika user mengetik angka selain 0–5
        print("⚠️ Pilihan tidak valid. Silakan coba lagi.")
        continue  # kembali ke awal loop

    # Setelah menampilkan hasil, tanya apakah ingin lanjut
    lanjut = input("\nIngin menghitung lagi? (y/n): ").lower()
    if lanjut != "y":
        print("\n👋 Program selesai. Sampai jumpa!")
        break
