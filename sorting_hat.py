# Write code below 💖
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("THE SORTING HAT")
print("Q1) Apakah Anda lebih suka Subuh atau Senja?")

print("  1) Subuh")
print("  2) Senja")

jawab = int(input("Masukan jawaban anda (1-2):  "))

if jawab == 1:
    gryffindor = gryffindor + 1
    ravenclaw = ravenclaw + 1
elif jawab == 2:
    hufflepuff = hufflepuff + 1
    slytherin = slytherin + 1
else:
    print("Salah Input!")

print("Q2) Ketika aku meninggal, aku ingin orang-orang mengingatku sebagai:")
print("  1) Yang Baik")
print("  2) Yang Hebat")
print("  3) Yang Bijak")
print("  4) Pemberani")

jawab = int(input("Masukkan Jawaban Anda (1-4): "))
if jawab == 1:
    hufflepuff = hufflepuff + 2
elif jawab == 2:
    slytherin = slytherin + 2
elif jawab == 3:
    ravenclaw = ravenclaw + 2
elif jawab == 4:
    gryffindor = gryffindor + 2
else:
    print("Salah Input!")

print(gryffindor)
print(slytherin)
print(hufflepuff)
print(ravenclaw)

print("Q3) Alat musik apa yang paling kamu sukai?")
print(" 1) Biola")
print(" 2) Gitar")
print(" 3) Piano")
print(" 4) Drum")

jawab = int(input("Masukkan Jawaban Anda (1-4) :  "))
if jawab == 1:
    slytherin = slytherin + 4
elif jawab == 2:
    hufflepuff = hufflepuff + 4
elif jawab == 3:
    ravenclaw = ravenclaw + 4
elif jawab == 4:
    gryffindor = gryffindor + 4
else:
    print("Salah Input!")

print("Gryffindor", gryffindor)
print("Slytherin", slytherin)
print("Hufflepuff", hufflepuff)
print("Ravenclaw", ravenclaw)
