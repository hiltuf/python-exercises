#Uppgift 5
#Uppgift 1: Extrahera delmängder
djur = ["hund", "katt", "kanin", "fågel", "orm", "fisk"]

print(djur[:3])
print(djur[3:])
print(djur[1:5])

#Uppgift 2: Hoppa över element
nummer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nummer[::2])
print(nummer[::3])

#Uppgift 3: Vända en lista
färger = ["röd", "grön", "blå", "gul", "svart"]

# Färger i omvänd ordning
omvänd_färger = färger[::-1]
print(omvänd_färger)

omvänd_sträng = "Python"[::-1]
print(omvänd_sträng) 

#Uppgift 4: Använda negativa index
veckodagar = ["måndag", "tisdag", "onsdag", "torsdag", "fredag", "lördag", "söndag"]

nyDagar = veckodagar[-3:]
print(nyDagar)

nyDagar = veckodagar[:-2]
print(nyDagar)

#Uppgift 5: Strängmanipulation med slicing
meddelande = "Välkommen till kursen"

changeMeddelande = meddelande[:9]
print(changeMeddelande)

changeMeddelande = meddelande[-6:]
print(changeMeddelande)

changeMeddelande = meddelande[::-1]
print(changeMeddelande)