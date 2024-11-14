#Uppgifter 1-10
#1. Variabler och Operatorer
sek = float(input("Ange beloppet i SEK: "))
usd_rate = sek * 0.11
eur_rate = sek * 0.095 

print(f"{sek} SEK är {usd_rate} USD")
print(f"{sek} SEK är {eur_rate} EUR")



#2. If-satser och Boolean
age = 24
is_Student = False 

if age <= 26 or is_Student:
    print("Berättigad till studentrabatt")
else: 
    print("Du är inte under 26 eller student")



#3. Listor och Loopar
filmList = ["Interstellar", "The Shawshank Redemption", "Star Wars: Episode VI - Return of the Jedi", "Inception"]

for film in filmList:
    print(film)
    if "Star" in film:
        print("Stjärnfilm!")



#4. Sets och Medlemskapsoperatorer
math_students = {"Alice", "Bob", "Charlie", "David", "Hilmer"}
science_students = {"Charlie", "David", "Eve", "Fiona", "Hilmer"}

both_courses = math_students & science_students
print("Elever i båda kurserna:", both_courses)

elev = "Bob"
if elev in both_courses:
    print(f"{elev} är med i båda kurserna")
else:
    print(f"{elev} är inte med i båda kurserna")



#5. Dictionary och If-satser
products = {
    'Mjölk': 13,
    'Bröd': 25,
    'Ägg': 19
}


product = "Bröd"
if product in products:
    print(f"{product} kostar: {products[product]}kr")
else:
    print(f"{product} finns ej i lager.")



#6. While-loopar och Aritmetiska Operationer
import random
startNumber = 20

while startNumber > 0:
    startNumber -= random.randint(1, 3)
    print(f"Nytt värde: {startNumber}")



#7. Strings och in Operator
ordLista = ["äpple", "banan", "körsbär", "druva"]

bokstav = (input("Ange en bokstav: "))

for ord in ordLista:
    if bokstav in ord:
        print(ord)



#8. Listor och Inbyggda Metoder
numbers = [10, -5, 7, -2, -20, 40]
negativaNumbers = []

for number in numbers:
    negativ = number < 0
    filter(negativ, numbers)
    if negativ:
        negativaNumbers.append(number)
print("Negativa tal:", negativaNumbers)
print("Antal negativa tal:", len(negativaNumbers))



#9. Tupler och Formatsträngar:
tuplBok = ('Jag är Zlatan', 'David Lagercrantz', 2012)
print(f"Boken {tuplBok[0]} är skriven av {tuplBok[1]} och publicerades år {tuplBok[2]}.")



# 10. Dictionaries och Loopar
elever = {
    'Hilmer': 5,
    'Jakob': 7,
    'August': 10
}

for namn, points in elever.items():
    print(f"{namn} fick {points} poäng")

medelpoints = sum(elever.values()) / len(elever)
print(f"Medelpoängen är {medelpoints:.2f}")
