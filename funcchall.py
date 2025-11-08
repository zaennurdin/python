# 🎮 KDA Calculator (tanpa pembagian jika d = 0)
# Materi: Functions + if + return


def kda(k, d, a):
    """
    Menghitung rasio KDA.
    Jika death (d) = 0, maka pembagian tidak dilakukan,
    dan hasilnya hanya (k + a) saja.
    """
    if d == 0:
        # Tidak ada pembagian, langsung return total kill + assist
        kda_ratio = k + a
    else:
        # Jika death tidak nol, hitung seperti biasa
        kda_ratio = (k + a) / d

    return kda_ratio


# -------------------------------------------------------
# Contoh penggunaan fungsi
# -------------------------------------------------------

# 1️⃣ Normal: ada death
print("KDA Player 1:", kda(10, 2, 5))  # (10+5)/2 = 7.5

# 2️⃣ Death 0 → pembagian tidak dilakukan
print("KDA Player 2:", kda(12, 0, 4))  # (12+4) = 16 (tanpa dibagi)

# 3️⃣ Death 1 → normal
print("KDA Player 3:", kda(8, 1, 6))  # (8+6)/1 = 14

# MoonPhase
# 🌕 Moon Phase Program
# Materi: Functions + if/elif/else + return
# 🌕 Moon Phase Program
# Materi: Functions + if/elif/else + return


def moon_phase(phase):
    """
    Menerima nama fase bulan (string),
    dan mengembalikan emoji sesuai fase tersebut.
    """
    if phase == "New Moon":
        return "🌑"
    elif phase == "Waxing Crescent":
        return "🌒"
    elif phase == "First Quarter":
        return "🌓"
    elif phase == "Waxing Gibbous":
        return "🌔"
    elif phase == "Full Moon":
        return "🌕"
    elif phase == "Waning Gibbous":
        return "🌖"
    elif phase == "Last Quarter":
        return "🌗"
    elif phase == "Waning Crescent":
        return "🌘"
    else:
        # Jika fase yang dikirim tidak cocok dengan daftar di atas
        return "Invalid moon phase"


# -------------------------------------------------------
# 🌙 Contoh Pengujian Fungsi (sesuai instruksi)
# -------------------------------------------------------

answer = moon_phase("New Moon")
print(answer)

# dog_year
# Write code below 💖

# 🐶 Dog Years Converter
# Materi: Functions + Parameters + Return + String Formatting


def dog_years(name, age):
    """
    Fungsi ini menghitung usia anjing dalam tahun manusia.
    name : nama anjing (string)
    age  : usia anjing dalam tahun anjing (integer)
    """
    human_years = age * 7  # 1 tahun anjing = 7 tahun manusia
    return f"{name} is {human_years} years old in human years."


# -------------------------------------------------------
# 🐾 Contoh Pengujian Fungsi
# -------------------------------------------------------
print(dog_years("Landon", 3))
print(dog_years("Red Bean", 6))
print(dog_years("Cooper", 2))
