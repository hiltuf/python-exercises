# #Python övningar

# #1. Enkel Räknare
# tal1 = int(input("Ange första tal: "))
# tal2 = int(input("Ange andra tal: "))

# operation = input("Ange matematisk operation (addition, subtraktion, multiplikation, division): ").lower()

# if "addition" in operation:
#     resultat = tal1 + tal2

# elif "subtraktion" in operation:
#     print(tal1 - tal2)
#     resultat = tal1 - tal2

# elif "multiplikation" in operation:
#     resultat = tal1 * tal2

# elif "division" in operation:
#     if tal2 == 0:
#         tal2 = int(input("Ange annat tal än noll: "))
#         resultat = tal1 / tal2
#     else:
#         resultat = tal1 / tal2
# else:
#     print("Fel")

# print("Resultat", resultat)

# # 2. Gissa Talet
# import random
# random_int = random.randint(1, 100)
# print(random_int)

# tries = 0
# max_tries = 5

# while max_tries > tries:
#     user_input = int(input("Gissa AI's nummer: "))
#     if user_input > random_int:
#         tries += 1
#         print('För högt')
#     elif user_input < random_int:
#         tries += 1
#         print('För lågt')
#     else:
#         won = True
#         print('Du gissade rätt!!!!')
#         break 

# if tries == 5:
#     print("Du har överstridigt antal försök: (Max: 5)")
# elif tries == 5 and won:
#     ""

# # 3. Lista Ord i Bokstavsordning
# mening = input("Skriv en mening: ")
# ord_lista = mening.lower().split()
# ord_lista.sort()

# sorterad_mening = " ".join(ord_lista)
# print("Ord i alfabetisk ordning:", sorterad_mening)

# # 4. Enkla Statistikberäkningar
# tal_input =  input("Skriv flera tal med ',' efter varje: ")
# tal_lista = [int(tal.strip()) for tal in tal_input.split(",")]

# medelvärde = sum(tal_lista) / len(tal_lista)
# minsta_tal = min(tal_lista)
# största_tal = max(tal_lista)
# summan = sum(tal_lista)

# print(f"Medelvärde: {medelvärde}")
# print(f"Minsta talet: {minsta_tal}")
# print(f"Största talet: {största_tal}")
# print(f"Summan av alla tal: {summan}")

# #5. Liten Frågesport
# poäng : int = 0

# question_lista : str = {
#     '(Lätt) Bilen är gul, vilken färg har den? A= Gul, B= Blå, C= Svart, D= Orange': 'a',
#     '(Medel) Du såg en fyrvägskorsning 100m bort, hur långt bort är du om du står 20m ifrån den? A= 50m, B= 120m, C= 100m, D= 20m': 'd',
#     '(Svår) Vad blir produkten av 2 och 5? A= 15, B= 7, C= 3, D= 10': 'd'
# }

# alternativ : str = 'Svarsalternativ: (A, B, C, D)'

# for which_question, answer in question_lista.items():
#         print("")
#         print(which_question)
#         print(alternativ)
#         print("")
#         user_input = input("Ange ditt svar: ").lower()
#         if user_input == answer:
#             print("Rätt alternativ!!!!!")
#             if "Lätt" in which_question:
#                 poäng += 1
#             elif "Medel" in which_question:
#                 poäng += 2
#             elif "Svår" in which_question:
#                 poäng += 3
#         else:   
#             print(f"Fel alternativ! Rätt alternativ var: {answer}.upper()")

# print("")
# print("Du fick totalt:", poäng, "poäng")

# # Funktioner
# # 1. Temperaturomvandlare

# def celsius():
#     print('Du valde Celsius')
#     temp_input : float = float(input('Ange temperatur i Celsius: '))
#     diff : float = (temp_input * 1.8) + 32.0
#     print("Fahrenheit: ", diff, "grader")

# def fahrenheit():
#     print('Du valde Fahrenheit')
#     temp_input : float = float(input('Ange temperatur i Fahrenheit: '))
#     diff : float = (temp_input - 32.0) / 1.8
#     print("Celsius: ", diff, "grader")

# omvandlare_input : str = input('Välj vilken konverting du vill göra: (Celsius, Fahrenheit)').lower()

# if omvandlare_input == "celsius":
#     celsius()
# elif omvandlare_input == "fahrenheit":
#     fahrenheit()
# else:
#     print("Ogiltig")

# #2. Enkla Textanalyser

# user_input : str = input("Skriv en mening: ")

# def count_words(user_input):
#     return len(user_input.split())

# def count_letters(user_input):
#     return sum(1 for char in user_input if char.isalpha())

# def longest_word(user_input):
#     words = user_input.split()
#     return max(words, key=len)

# print(f"Antal ord: {count_words(user_input)}")
# print(f"Antal ord: { count_letters(user_input)}")
# print(f"Längsta ordet: '{longest_word(user_input)}'")

# # 3. Beräkna Area och Omkrets av en Cirkel
# import math

# def omkrets(r):
#     result = 2 * r * math.pi 
#     return f"{result:.2f}"

# def area(r):
#     result = math.pi * r ** 2 
#     return f"{result:.2f}"

# r : int = int(input("Ange radie för en cirkel i (cm): "))

# if r > 0:
#     print(f"Omkrets: {omkrets(r)}cm")
#     print(f"Omkrets: {area(r)}cm")
# else:
#     print("Ogiligt radie, måste vara positivt")

#4. Multiplikationstabell'
# def multitabell(tal, multi):
#     for i in range(1, multi + 1):
#         print(f"{tal} x {i} = {tal * i}")

# tal: int = int(input("Skriv ett tal: "))
# multi: int = int(input("Ange hur långt du vill se: "))

# multitabell(tal, multi)

# #5. Palindrome Checker

# def isPalindrome(text_input):
#     return text_input == text_input[::-1]

# text_input = input("Skriv ett ord: ")
# ans = isPalindrome(text_input)

# if ans:
#     print("Palindrom")
# else:
#     print("Ingen palindrom")

#OOP

#1. 1. Kunddatabas