import random

rating = float(input("Masukan Nilai Review:"))
if rating > 4.5:
    print("Extraordinary")
elif rating > 4:
    print("Excellent")
elif rating > 3:
    print("Good")
elif rating > 2:
    print("Fair")
else:
    print("Poor")

# Write code below 💖

# Write code below 💖

grade = int(input("Insert Grade Value:"))
if grade == 9:
    print("Freshman")
elif grade == 10:
    print("Sophomore")
elif grade == 11:
    print("Junior")
elif grade == 12:
    print("Senior")
else:
    print("TBD")


num = random.randint(0, 5)

if num == 0:
    print("Flamingos turn pink from eating shrimp.")
elif num == 1:
    print("The only food that doesn't spoil is honey.")
elif num == 2:
    print("Shrimp can only swim backwards.")
elif num == 3:
    print("A taste bud's life span is about 10 days.")
elif num == 4:
    print("It is impossible to sneeze while sleeping.")
elif num == 5:
    print("It is illegal to sing off-key in North Carolina.")
else:
    print("TBD")

bulan = int(input("Masukan Angka Bulan:"))
if bulan == 1 or bulan == 2 or bulan == 3:
    print("Winter 🌨️")
elif bulan == 4 or bulan == 5 or bulan == 6:
    print("Spring 🌱")
elif bulan == 7 or bulan == 8 or bulan == 9:
    print("Summer 🌞")
elif bulan == 10 or bulan == 11 or bulan == 12:
    print("Autumn 🍂")
else:
    print("Invalid")


# Write code below 💖

print("Welcome to Our Weight Conversion in another planet Program")
earth_weight = float(input("Enter your weight: "))
print("CHOOSE THE DESTINATED PLANET")
print("1. Merkurius")
print("2. Venus")
print("3. Mars")
print("4. Jupiter")
print("5. Saturnus")
print("6. Uranus")
print("7. Neptunus")
planet = int(input("Enter the planet number: "))

if planet == 1:
    destination_weight = earth_weight * 0.38
    print(destination_weight)
elif planet == 2:
    destination_weight = earth_weight * 0.91
    print(destination_weight)
elif planet == 3:
    destination_weight = earth_weight * 0.38
    print(destination_weight)
elif planet == 4:
    destination_weight = earth_weight * 2.53
    print(destination_weight)
elif planet == 5:
    destination_weight = earth_weight * 1.07
    print(destination_weight)
elif planet == 6:
    destination_weight = earth_weight * 0.89
    print(destination_weight)
elif planet == 7:
    destination_weight = earth_weight * 1.14
    print(destination_weight)
else:
    print("Invalid")
