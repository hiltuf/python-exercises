#Uppgifter om Funktioner

#1. Definiera och Anropa en Funktion
def heyWorld():
    print('Hej, världen!')

heyWorld()

#2. Funktion med Parametrar
def sumNumbers(num1, num2):
    return num1 + num2

resultat = sumNumbers(2, 4)
print(resultat)

#3. Funktion som Returnerar Värde
def multiNumbers(first, second):
    return first * second

multiResultat = multiNumbers(10, 5)
print(multiResultat)

#4. Funktion utan Parametrar

def preDefined():
    return 42

preResult = preDefined()
print(preResult)

#5. Funktion med Flera Parametrar
def treParameters(namn, age, stad):
    return f"Hej, jag heter {namn}, jag är {age} år gammal och bor i {stad}"

exempel = treParameters('Hilmer', 21, 'Stockholm')
print(exempel)

#6. Funktion med Defaultvärden
def defaultParameters(namn, age=30):
    return f"Hej, jag heter {namn}, jag är {age}"

result = defaultParameters('Hilmer')
missingResult = defaultParameters('Hilmer', 21)
print(result)
print(missingResult)

#7. Beräkna Omkretsen av en Cirkel
import math

def getOmkrets(radie):
    omkrets = 2 * math.pi * radie
    return omkrets

resultOmkrets = getOmkrets(5)
print("Omkrets:", resultOmkrets)

#8. Använd Funktioner i Listor
def listaSum(listTest):
    return sum(listTest)

listTest = listaSum([2, 4, 6, 7])
print("Summan av listan:", listTest)

#9. Funktion med Villkor (If-satser)
def tempCheck(temp):
    if temp > 25:
        return 'Varm'
    elif temp < 10:
        return 'Kall'
    else:
        return 'Mild'

actualTemp = tempCheck(26)
print("Värmen är:", actualTemp)

actualTemp = tempCheck(9)
print("Värmen är:", actualTemp)

#10. Funktion som Tar In Input från Användaren
def inputColor():
    color = input("Vad är din favoritfärg? ")
    print(f"Din favoritfärg är {color}")

inputColor()