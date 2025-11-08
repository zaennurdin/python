# hash_explorer.py
# 🔐 Program interaktif untuk eksplorasi hashing dengan hashlib

import hashlib

# Daftar algoritma populer dan penjelasannya
algorithms_info = {
    "md5": "MD5: cepat tapi tidak aman, panjang hash 128-bit, sering dipakai untuk checksum.",
    "sha1": "SHA1: lebih aman dari MD5 tapi sudah tidak direkomendasikan untuk keamanan tinggi, 160-bit.",
    "sha224": "SHA224: versi pendek dari SHA256, hash 224-bit.",
    "sha256": "SHA256: aman & populer, hash 256-bit, sering digunakan di blockchain.",
    "sha384": "SHA384: versi panjang SHA256, hash 384-bit.",
    "sha512": "SHA512: hash 512-bit, sangat aman untuk data penting.",
    "sha3_256": "SHA3-256: algoritma modern SHA-3, hash 256-bit.",
    "blake2b": "BLAKE2b: cepat & aman, hash 512-bit, cocok untuk file besar.",
    "blake2s": "BLAKE2s: versi 256-bit dari BLAKE2, cepat untuk embedded systems.",
}

# Menu interaktif
print("🔐 Selamat datang di Hash Explorer!")
print("Kamu bisa memasukkan teks dan memilih algoritma hashing.")
print("Ketik 'exit' untuk keluar.\n")

while True:
    # Input teks
    teks = input("Masukkan teks yang ingin di-hash: ").strip()
    if teks.lower() == "exit":
        print("👋 Terima kasih! Program selesai.")
        break

    print("\nPilih algoritma hashing:")
    for i, alg in enumerate(algorithms_info.keys(), start=1):
        print(f"{i}. {alg}")

    pilihan = input("Masukkan nama algoritma (misal: sha256): ").strip().lower()

    if pilihan not in algorithms_info:
        print("❌ Algoritma tidak ditemukan. Coba lagi.\n")
        continue

    # Ambil fungsi hash dari hashlib
    hash_func = getattr(hashlib, pilihan)
    hash_obj = hash_func(teks.encode())  # teks harus diubah ke bytes
    hash_hex = hash_obj.hexdigest()

    # Tampilkan hasil
    print("\n✅ Hasil hash:")
    print(f"Teks asli      : {teks}")
    print(f"Algoritma      : {pilihan}")
    print(f"Penjelasan     : {algorithms_info[pilihan]}")
    print(f"Hasil hash     : {hash_hex}\n")
    print("=" * 50 + "\n")
