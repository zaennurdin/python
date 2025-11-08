tebak = 0
coba = 0

while tebak != 6 and coba < 5:
    tebak = int(input("Tebak angka: "))
    coba = coba + 1
    if (
        tebak != 6 and coba < 5
    ):  # Tambahkan notifikasi jika salah dan masih ada kesempatan
        print("Salah! Coba lagi.")  # Notifikasi salah

if tebak != 6:
    print("Kamu habis coba.")
else:
    print("Kamu betul!")
