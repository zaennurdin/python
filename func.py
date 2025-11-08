# dry.py
# 🔍 Exploring Python Built-in Functions
# Tema: Memahami fungsi-fungsi bawaan (built-in functions) Python

# 1️⃣ len()
# Mengembalikan panjang (jumlah item) dari objek seperti list, string, tuple, dll.
playlist = ["Novo Amor", "Mitski", "Radiohead"]
print("len() → Jumlah item di playlist:", len(playlist))
# Output: 3


# 2️⃣ sum()
# Menjumlahkan semua angka dalam list atau tuple.
angka = [10, 20, 30, 40]
print("sum() → Total angka:", sum(angka))
# Output: 100


# 3️⃣ max()
# Mengembalikan nilai terbesar dari list atau tuple.
nilai = [3, 8, 2, 10, 5]
print("max() → Nilai tertinggi:", max(nilai))
# Output: 10


# 4️⃣ enumerate()
# Mengembalikan pasangan (index, nilai) dari sebuah list.
# Biasanya digunakan dalam perulangan agar tahu nomor item dan isinya.
lagu = ["Anchor", "Carry You", "State Lines"]
print("enumerate() → Menampilkan lagu dengan nomor urut:")
for nomor, judul in enumerate(lagu, start=1):
    print(f"{nomor}. {judul}")
# Output:
# 1. Anchor
# 2. Carry You
# 3. State Lines


# 5️⃣ bin()
# Mengubah bilangan desimal menjadi biner (base 2)
# Hasil selalu diawali dengan '0b' sebagai penanda biner
desimal = 25
print("bin() → Bentuk biner dari 25:", bin(desimal))
# Output: 0b11001


# 6️⃣ hex() — fungsi baru!
# Mengubah bilangan desimal menjadi heksadesimal (base 16)
# Hasil diawali dengan '0x' sebagai penanda heksadesimal
desimal2 = 255
print("hex() → Bentuk heksadesimal dari 255:", hex(desimal2))
# Output: 0xff
