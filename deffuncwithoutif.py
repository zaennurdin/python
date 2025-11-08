import random


def fortune():
    # List ramalan
    fortunes = [
        "Don't pursue happiness – create it.",
        "All things are difficult before they are easy.",
        "The early bird gets the worm, but the second mouse gets the cheese.",
        "Someone in your life needs a letter from you.",
        "Don't just think. Act!",
        "Your heart will skip a beat.",
        "The fortune you search for is in another cookie.",
        "Help! I'm being held prisoner in a Chinese bakery!",
    ]

    # Ambil angka acak sesuai index list
    n = random.randint(0, len(fortunes) - 1)

    # Tampilkan ramalan
    print(fortunes[n])


# Memanggil fungsi fortune() tiga kali
for i in range(3):
    fortune()
