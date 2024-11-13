#Uppgift 1: Lista – Ändra och lägg till element
lista = [10, 20, 30, 40]
lista[0] = 5

lista.append(50)
lista.remove(lista[1])

print(lista)

#Uppgift 2: Tupl – Åtkomst och felsökning
tupl = (1, 2, 3, 4)
print(tupl[2])
#tupl[0] = 0 (Går inte eftersom indexen i tupl:en är constant)
tuplsingle = (100,)
print(tuplsingle)

#Uppgift 3: Set – Lägg till och ta bort element
set = {1, 2, 3, 4, 5}
set.add(6)
set.remove(3)
print(set)
#print(set[2]) (Går inte eftersom set inte har någon bestämd ordning)

#Uppgift 4: Dictionary – Nyckel-värde-par
dictionary = {'name': 'Alice', 'age': 25, 'city': 'Stockholm'}
print(dictionary['name'])
dictionary['country'] = 'Sweden'
print(dictionary)
del dictionary['city']
print(dictionary)

#Uppgift 5: Villkor (if-satser)
ages = [18, 25, 30, 16, 21]

if ages[0] >= 18:
    print(f"{ages[0]}: Är vuxen")
else:
    print(f"{ages[0]}: Är inte vuxen")

if ages[1] >= 18:
    print(f"{ages[1]}: Är vuxen")
else:
    print(f"{ages[1]}: Är inte vuxen")

if ages[2] >= 18:
    print(f"{ages[2]}: Är vuxen")
else:
    print(f"{ages[2]}: Är inte vuxen")

if ages[3] >= 18:
    print(f"{ages[3]}: Är vuxen")
else:
    print(f"{ages[3]}: Är inte vuxen")

if ages[4] >= 18:
    print(f"{ages[4]}: Är vuxen")
else:
    print(f"{ages[4]}: Är inte vuxen")
