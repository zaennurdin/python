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

    # Ambil angka acak antara 0 sampai 7
    n = random.randint(0, len(fortunes) - 1)

    # Tampilkan fortune sesuai angka acak
    if n == 0:
        print(fortunes[0])
    elif n == 1:
        print(fortunes[1])
    elif n == 2:
        print(fortunes[2])
    elif n == 3:
        print(fortunes[3])
    elif n == 4:
        print(fortunes[4])
    elif n == 5:
        print(fortunes[5])
    elif n == 6:
        print(fortunes[6])
    else:
        print(fortunes[7])


# Memanggil fungsi fortune() tiga kali
fortune()
fortune()
fortune()
