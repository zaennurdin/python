import random

for n in range(10, 0, -1):
    print(n)

print("Happy New Year! 🥳")

total = 0


while total != 2:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print("Nope")

if total == 2:
    print("Snake Eyes")

# 🌟 Tangga Bintang
# Gunakan for loop, range(), dan print() untuk membuat tangga dengan 24 baris

for i in range(1, 25):  # Mulai dari 1 sampai 24
    print("* " * i)  # Cetak i tanda bintang, masing-masing diikuti spasi

# Write code below 💖

# 💡 Program menghitung jumlah kuadrat dari 1 hingga n

# 1️⃣ Meminta input dari user dan ubah ke integer
number = int(input("Masukkan sebuah bilangan bulat: "))

# 2️⃣ Inisialisasi variabel total untuk menyimpan hasil penjumlahan
total = 0

# 3️⃣ Gunakan for loop untuk menjumlahkan setiap bilangan kuadrat
for i in range(1, number + 1):  # dimulai dari 1 sampai number
    total += i**2  # i**2 artinya i pangkat 2 (kuadrat)

# 4️⃣ Cetak hasil akhirnya
print(int(total))
