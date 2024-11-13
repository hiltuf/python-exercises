#Uppgift 1: Kontrollera om en person är vuxen
age = 21

if age >= 18:
    print("Du är vuxen!")
else:
    print("Du är inte vuxen än!")

#Uppgift 2: Jämför två tal
num1 = 5
num2 = 8

if num1 > num2:
    print("Första talet är större")
elif num2 > num1:
    print("Andra talet är större")
else:
    print("Tal är lika")

#Uppgift 3: Bestäm om ett tal är positivt, negativt eller noll
number = -2
if number > 0:
    print("Positivt tal")
elif number < 0:
    print("Negativt tal")
else:
    print("Talet är noll")

#Uppgift 4: Betygskontroll
grade = 50

if grade > 50:
    print("Du klarade tentan!")
else:
    print("Tyvärr, du klarade inte tentan!")

#Uppgift 5: Ålderskategori
age = 15

if age >= 20:
    print("Vuxen")
elif age >= 13 and age <= 19:
    print("Tonåring")
else:
    print("Barn")