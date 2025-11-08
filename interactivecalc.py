# 🔢 Interactive Calculator
# Program ini memungkinkan pengguna memilih operasi matematika dan menghitung hasilnya.

# Kita definisikan fungsi-fungsi dasar dulu
# Masing-masing fungsi menerima 2 parameter (a dan b) dan MENGEMBALIKAN hasil (bukan print)
def add(a, b):
    return a + b  # Mengembalikan hasil penjumlahan

def subtract(a, b):
    return a - b  # Mengembalikan hasil pengurangan

def multiply(a, b):
    return a * b  # Mengembalikan hasil perkalian

def divide(a, b):
    return a / b  # Mengembalikan hasil pembagian

def exp(a, b):
    return a ** b  # Mengembalikan hasil pangkat


# ====================================================
# 🧠 Bagian utama program
# ====================================================

print("=== Kalkulator Interaktif Python ===")
print("Operasi yang tersedia:")
print("1. Tambah (+)")
print("2. Kurang (-)")
print("3. Kali (*)")
print("4. Bagi (/)")
print("5. Pangkat (**)")

# Meminta input dari pengguna
# input() akan selalu menghasilkan string, jadi kita ubah ke float supaya bisa dihitung
angka1 = float(input("\nMasukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Meminta pilihan operasi
pilihan = input("Pilih operasi (1/2/3/4/5): ")

# Gunakan struktur if/elif/else untuk menentukan operasi mana yang dijalankan
if pilihan == "1":
    hasil = add(angka1, angka2)
    print(f"\nHasil: {angka1} + {angka2} = {hasil}")

elif pilihan == "2":
    hasil = subtract(angka1, angka2)
    print(f"\nHasil: {angka1} - {angka2} = {hasil}")

elif pilihan == "3":
    hasil = multiply(angka1, angka2)
    print(f"\nHasil: {angka1} × {angka2} = {hasil}")

elif pilihan == "4":
    # Kita tambahkan sedikit logika agar tidak membagi dengan nol
    if angka2 == 0:
        print("\n❌ Tidak bisa membagi dengan nol!")
    else:
        hasil = divide(angka1, angka2)
        print(f"\nHasil: {angka1} ÷ {angka2} = {hasil}")

elif pilihan == "5":
    hasil = exp(angka1, angka2)
    print(f"\nHasil: {angka1} ^ {angka2} = {hasil}")

else:
    print("\n⚠️ Pilihan tidak valid. Silakan jalankan ulang program.")

print("\nTerima kasih telah menggunakan kalkulator ini! 😊")
