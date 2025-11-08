# 📈 stock_analysis.py
# Analisis sederhana harga saham dengan tiga fungsi utama:
# 1. price_at(i)
# 2. max_price(a, b)
# 3. min_price(a, b)

# Data harga saham selama 20 hari
stock_prices = [
    34.68,
    36.09,
    34.94,
    33.97,
    34.68,
    35.82,
    43.41,
    44.29,
    44.65,
    53.56,
    49.85,
    48.71,
    48.71,
    49.94,
    48.53,
    47.03,
    46.59,
    48.62,
    44.21,
    47.21,
]


# ======================================================
# 1️⃣ Fungsi price_at(i)
# Mengembalikan harga saham pada hari ke-i
# ======================================================
def price_at(i):
    # i dimulai dari 1, jadi kita pakai i-1 karena index list mulai dari 0
    return stock_prices[i - 1]


# ======================================================
# 2️⃣ Fungsi max_price(a, b)
# Mengembalikan harga maksimum dari hari ke-a sampai ke-b
# ======================================================
def max_price(a, b):
    # Gunakan slicing list dan fungsi bawaan max()
    return max(stock_prices[a - 1 : b])


# ======================================================
# 3️⃣ Fungsi min_price(a, b)
# Mengembalikan harga minimum dari hari ke-a sampai ke-b
# ======================================================
def min_price(a, b):
    # Gunakan slicing list dan fungsi bawaan min()
    return min(stock_prices[a - 1 : b])


# ======================================================
# 🚀 Pengujian fungsi
# ======================================================

print("📊 Analisis Data Harga Saham\n")

# 1. Harga pada hari ke-5
print("Harga hari ke-5:", price_at(5))

# 2. Harga maksimum dari hari 1–10
print("Harga maksimum antara hari ke-1 dan 10:", max_price(1, 10))

# 3. Harga minimum dari hari 11–20
print("Harga minimum antara hari ke-11 dan 20:", min_price(11, 20))

# 4. Uji tambahan untuk memastikan fungsi bekerja
print("\nHarga hari ke-20:", price_at(20))
print("Harga maksimum 5–15:", max_price(5, 15))
print("Harga minimum 1–5:", min_price(1, 5))
