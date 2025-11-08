# Write code below 💖

best_pictures = [
    "2024 - Anora",
    "2023 - Oppenheimer",
    "2022 - Everything Everywhere All at Once",
    "2021 - CODA",
    "2020 - Nomadland",
    "2019 - Parasite",
    "2018 - Green Book",
    "2017 - The Shape of Water",
    "2016 - Moonlight",
    "2015 - Spotlight",
    "2014 - Birdman",
    "2013 - 12 Years a Slave",
    "2012 - Argo",
    "2011 - The Artist",
]

print(best_pictures)

# Split The Bill
bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]
total = 0
for item in bill:
    total = total + item
    my_share = total / 4
print(total)
print(my_share)

# DNA Sequence
# 🧬 Program pencarian urutan DNA tiga huruf

# 🧬 DNA Sequence Finder

# Daftar DNA 3-huruf
dna_sequence = [
    "GCT",
    "AGC",
    "AGG",
    "TAA",
    "ACT",
    "CAT",
    "TAT",
    "CCC",
    "ACG",
    "GAA",
    "ACC",
    "GGA",
]

# ✅ Harus 3 karakter, hanya berisi A, T, C, atau G
item_to_find = "TGA"  # <-- kamu bisa ubah ke kombinasi lain seperti 'CAT' atau 'GCT'

# Boolean penanda ditemukan atau tidak
item_found = False

# Loop untuk mencari item dalam list
for item in dna_sequence:
    if item == item_to_find:
        item_found = True

# Cek hasil akhir
if item_found:
    print("Item Found! 🧬")
else:
    print("Item not found. ❌")
