# ### **Customer**

# - `Customer`klassen ska ha följande attribut: KLART
#     - `name`: kundens namn. KLART
#     - `email`: kundens e-postadress. KLART
#     - `phone`: kundens telefonnummer. KLART
#     - `interactions`: en lista över alla interaktioner med kunden. KLART
#     - `last_interaction`: datum och tid för kundens senaste interaktion (initialt `None`). KLART
# - `Customer`klassen ska även ha följande metoder:
#     - `add_interaction`: Lägger till en interaktion med kunden och uppdaterar `last_interaction`. KLART
#     - `calculate_days_since_last_interaction`: Räknar antalet dagar sedan kundens senaste interaktion (eller returnerar `None` om det inte finns några interaktioner). KLART

# ### **CustomerDataSystem**

# - `CustomerDataSystem`klassen ska ha två attribut:
#     - `name`: namnet på företaget/systemet. KLART
#     - `customers`: en lista över alla kunder i systemet (innehåller `Customer`objekt). KLART
# - Klassen ska ha metoder för att utföra följande:
#     - Lägga till en kund. KLART
#     - Ta bort en kund. KLART
  #   - Uppdatera en kunds kontaktinformation (telefon och/eller e-postadress). KLART (GJORDE ENBART TELEFON)
    #  - Lägga till en interaktion för en specifik kund. klart
  #  - Hämta en lista över alla interaktioner för en specifik kund. KLART
#     - Skriva ut en lista över alla kunder i systemet. KLART
    #  - Vid varje metodanrop ska ett meddelande skrivas ut om vad som skett (t.ex. *"Ny kund med namn X har lagts till"*). ISH KLAR/FIXA


### **Metoddetaljer**

# - Metoden för att lägga till en kund ska skapa ett nytt `Customer`objekt och lägga till det i listan. KLART
# - Kontrollera vid tillägg av kund att e-postadressen inte redan finns i systemet. Om den finns, kasta ett undantag (t.ex. `ValueError`).
# - När en interaktion läggs till, ska det aktuella datumet och tiden lagras i kundens `last_interaction`. KLART
# - När en kund tas bort, kontrollera att kunden existerar i systemet. Om inte, kasta ett undantag (t.ex. `KeyError`).

# https://willandskill.notion.site/Exception-handling-undantagshantering-f512987dadf547ca921e1dfbe1299563