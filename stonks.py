# Stonks 📈
# Codédex
# Program ini digunakan untuk menganalisis harga saham (stock prices)
# dengan mencari harga di hari tertentu, harga maksimum, dan harga minimum
# menggunakan fungsi dan konsep return.

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


# -------------------------------------------------------------
# 1️⃣ Fungsi price_at(i)
# Mengembalikan harga saham pada hari ke-i
# -------------------------------------------------------------
def price_at(i):
    # Karena list dimulai dari index 0,
    # maka kita pakai i-1 agar hari ke-1 mengacu ke index 0
    return stock_prices[i - 1]


# -------------------------------------------------------------
# 2️⃣ Fungsi max_price(a, b)
# Menghitung harga maksimum dari hari ke-a sampai ke-b
# -------------------------------------------------------------
def max_price(a, b):
    mx = 0  # variabel untuk menyimpan nilai maksimum sementara (mulai dari 0)
    # Perulangan dari hari ke-a sampai ke-b
    for i in range(a, b + 1):
        # Ambil harga hari ke-i menggunakan fungsi price_at()
        # dan bandingkan dengan nilai maksimum sebelumnya
        # Fungsi max(x, y) akan mengembalikan nilai terbesar antara x dan y
        mx = max(mx, price_at(i))
    # Setelah loop selesai, kembalikan hasil maksimum
    return mx


# -------------------------------------------------------------
# 3️⃣ Fungsi min_price(a, b)
# Menghitung harga minimum dari hari ke-a sampai ke-b
# -------------------------------------------------------------
def min_price(a, b):
    # Nilai awal (mn) diambil dari harga pada hari ke-a
    # Supaya dibandingkannya dengan harga yang valid dari rentang yang sama
    mn = price_at(a)
    # Loop dari hari ke-a sampai ke-b
    for i in range(a, b + 1):
        # Fungsi min(x, y) mengembalikan nilai terkecil dari dua nilai
        mn = min(mn, price_at(i))
    # Setelah loop selesai, kembalikan nilai minimum
    return mn


# -------------------------------------------------------------
# 4️⃣ Pengujian fungsi
# -------------------------------------------------------------

# Cetak harga maksimum dari hari ke-1 sampai ke-15
print(max_price(1, 15))  # Harusnya mengembalikan nilai tertinggi di rentang hari 1–15

# Cetak harga minimum dari hari ke-5 sampai ke-10
print(min_price(5, 10))  # Harusnya mengembalikan harga terendah di rentang hari 5–10

# Cetak harga saham pada hari ke-3
print(price_at(3))  # Mengembalikan harga pada_
