import time

# Variabel awal
jam = 6
energi = 100
lapar = 50
hari = True

print("==============================")
print("Selamat datang di: SEHARI DALAM HIDUPMU 🌞")
print("==============================\n")

print("Kamu bangun di pagi hari, siap memulai hari.")
time.sleep(1)

# Loop kehidupan sehari
while hari:
    print(f"\n⏰ Jam: {jam}:00 | ⚡ Energi: {energi} | 🍔 Lapar: {lapar}")
    print("-------------------------------------")

    # Pilihan aksi tergantung waktu
    if jam < 9:
        print("1. Sarapan")
        print("2. Tidur lagi")
        print("3. Langsung berangkat kerja")
    elif jam < 17:
        print("1. Bekerja")
        print("2. Istirahat sebentar")
        print("3. Makan siang")
    else:
        print("1. Makan malam")
        print("2. Main game")
        print("3. Tidur malam")

    pilihan = input("Apa yang kamu lakukan? (1/2/3): ")

    # PAGI
    if jam < 9:
        if pilihan == "1":
            print("🍞 Kamu sarapan roti dan teh hangat. Energi naik!")
            energi += 10
            lapar -= 30
        elif pilihan == "2":
            print("💤 Kamu tidur lagi sebentar...")
            energi += 20
            jam += 1
        elif pilihan == "3":
            print("🚶 Kamu berangkat kerja tanpa sarapan...")
            energi -= 10
            lapar += 10
        else:
            print("Kamu bingung mau ngapain.")
        jam += 1

    # SIANG
    elif jam < 17:
        if pilihan == "1":
            print("💻 Kamu bekerja keras di kantor.")
            energi -= 20
            lapar += 20
            jam += 2
        elif pilihan == "2":
            print("😴 Kamu istirahat sebentar di ruang istirahat.")
            energi += 10
            jam += 1
        elif pilihan == "3":
            print("🍛 Kamu makan siang enak di warung.")
            lapar -= 30
            energi += 5
            jam += 1
        else:
            print("Kamu bingung... waktu terus berjalan.")
            jam += 1

    # MALAM
    else:
        if pilihan == "1":
            print("🍜 Kamu makan malam bersama keluarga.")
            lapar -= 20
            energi += 5
            jam += 1
        elif pilihan == "2":
            print("🎮 Kamu bermain game online sampai lupa waktu...")
            energi -= 30
            lapar += 10
            jam += 2
        elif pilihan == "3":
            print("😴 Kamu memutuskan untuk tidur malam.")
            energi += 40
            jam = 6  # kembali ke pagi
            print("\n🌞 Kamu bangun keesokan harinya!")
        else:
            print("Kamu melamun sendirian...")
            jam += 1

    # Kondisi akhir/habis energi
    if energi <= 0:
        print("\n😵 Kamu kelelahan dan pingsan! Game Over.")
        hari = False
    elif lapar >= 100:
        print("\n🤢 Kamu kelaparan dan tidak kuat lagi. Game Over.")
        hari = False
    elif jam >= 24:
        print("\n🌙 Hari telah berakhir. Waktu tidur...")
        hari = False

    time.sleep(1)

print("\nTerima kasih sudah bermain!")
