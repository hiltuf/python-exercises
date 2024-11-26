# #Mer Uppgifter

# #Uppgift 1
# valuta_kurs = {"USD": 0.1, "EUR": 0.09, "GBP": 0.08}

# sek_input = int(input('Ange en summa i SEK: '))

# for valuta, kurs in valuta_kurs.items():
#     convert = kurs * sek_input
#     print(f"{sek_input} SEK är lika med {convert} {valuta}")

# #Uppgift 2
# age = int(input("Ange din ålder: "))
# roll = input("Ange din sysselsättning (Student, Arbetande, Pensionär): ").lower()


# if age < 18:
#     category = "Ungdom"
# elif age < 65:    
#     category = "Vuxen"
# else:  
#     category = "Pensionär"

# if roll == "student":
#     print(f"Du är en {category} och student.")
# elif roll == "arbetande":
#     print(f"Du är en {category} och arbetar.")
# else:
#     print(f"Du är en {category} och pensionär.")

# #Uppgift 3
# movies = {}
# print("Ange dina favoritfilmer och deras genre. Skriv 'stopp' för att sluta.")
# while True:
#     title = input("Ange filmens titel: ")
#     if title.lower() == "stopp":
#         break
#     genre = input("Ange filmens genre: ")
#     movies[title] = genre

# favorite_genre = input("Ange din favoritgenre: ").lower()

# for title, genre in movies.items():
#     if genre.lower() == favorite_genre:
#         print(f"{title} är i din favoritgenre!")
#     else:
#         print(f"{title} är inte i din favoritgenre.")

# Uppgift 4

# science_students = set(input("Naturvetenskap, Ange namn på eleverna (använd komma efter varje namn): ").split(", "))
# math_students = set(input("Matematik, Ange namn på eleverna (använd komma efter varje namn): ").split(", "))
# art_students = set(input("Konst, Ange namn på eleverna (använd komma efter varje namn): ").split(", "))

# multiple_subjects = (science_students & math_students) | (science_students & art_students) | (math_students & art_students)
# print(f"Elever som är registrerade i mer än ett ämne: {', '.join(multiple_subjects)}")

