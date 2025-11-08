import random

print("==================")  # Judul
print("Batu Gunting Kertas Kadal Robot")
print("==================")
pilihan = ["Batu", "Gunting", "Kertas", "Kadal", "Robot"]
menang_atas = {
    "Batu": ["Gunting", "Kadal"],
    "Gunting": ["Kertas", "Kadal"],
    "Kertas": ["Batu", "Robot"],
    "Kadal": ["Kertas", "Robot"],
    "Robot": ["Gunting", "Batu"],
}
print("===========================")
print("BATU GUNTING KERTAS KADAL ROBOT")
print("===========================")
print("Pilih Salah Satu : Batu /Gunting /Kertas /Kadal /Robot")
print("===========================")

player = input("Masukkan pilihan kamu: ").lower()
komputer = random.choice(pilihan)

print(f"\nKamu memilih: {player}")
print(f"Komputer memilih: {komputer}")

if player == komputer:
    print("Hasil: Seri 🤝")
elif komputer in menang_atas[player]:
    print("Hasil: Kamu Menang! 🎉")
else:
    print("Hasil: Kamu Kalah 😢")
