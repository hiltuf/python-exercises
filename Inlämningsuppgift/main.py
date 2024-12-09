from datetime import datetime

class Customer:
    def __init__(self, name, email, phone, interactions=None, last_interaction=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.interactions = interactions if interactions is not None else []
        self.last_interaction = last_interaction  # Datum och tid för senaste interaktion

    def add_interaction(self, interaction):
        self.interactions.append(interaction)
        self.last_interaction = datetime.now()  # Sätt senaste interaktionen till nuvarande tid
        print(f"Ny interaktion tillagd för {self.name}: {interaction}")
        print(f"Senaste interaktionen uppdaterad till: {self.last_interaction}")

    def calculate_days_since_last_interaction(self):
        if self.last_interaction is None:
            print(f"Ingen interaktion för {self.name}.")
            return None
        print(f"Senaste interaktionen (datum & tid) för {self.name}: {self.last_interaction}")
        days_since = (datetime.now() - self.last_interaction).days
        print(f"Senaste interaktion i dagar för {self.name}: {days_since}")
        return days_since
    



class CustomerDataSystem:
    def __init__(self, name, customers=None):
        self.name = name
        self.customers = customers if customers is not None else []  # Lista för att hålla Customer-objekt

    def add_customer(self, customer):
        self.customers.append(customer)  # Lägg till Customer-objekt i listan
        print(f"Kund {customer.name} med e-post {customer.email} har lagts till.")

    def remove_customer(self, email):
        # Hitta kund baserat på e-post
        for customer in self.customers:
            if customer.email == email:
                self.customers.remove(customer)
                print(f"Kund {customer.name} med e-post {email} har tagits bort.")
                return
        print(f"Ingen kund med e-post {email} hittades.")

    def update_customer(self, email):
        # Hitta kund baserat på e-post
        for customer in self.customers:
            if customer.email == email:
                print(f"Kund {customer.name} telefonnummer: {customer.phone}")
                customer.phone = input(f'Ange nya telefonnumret åt {customer.name}: ')
                print(f"Kund {customer.name} telefonnummer har ändrats till: {customer.phone}")
                return
        print(f"Ingen kund med e-post {email} hittades.")

    def add_specific_interaction(self, email, interaction):
        for customer in self.customers:
            if customer.email == email:
                customer.interactions.append(interaction)
                print(f'Kund {customer.name} har en ny interaktion: {interaction}')
                days_since = (datetime.now() - customer.last_interaction).days
                print(f"Senaste interaktion i dagar för {customer.name}: {days_since}")
    
    def customer_interactions(self, email):
        for customer in self.customers:
            if customer.email == email:
                if not customer.interactions:
                    print(f'Kund {customer.name} har inga interaktioner')
                else:
                    print(f'Kund {customer.name} interaktioner: {customer.interactions}')


    def list_customers(self):
        if not self.customers:
            print("Det finns inga kunder i systemet.")
        else:
            print("Lista över alla kunder:")
            for customer in self.customers:
                print(f"- {customer.name} telefon: {customer.phone}")












# Testfall
C1 = Customer('Hilmer', 'hilmer@mail.com', '3000')
C2 = Customer('Jakob', 'jakob@mail.com', '2000')
C3 = Customer('Felix', 'felix@mail.com', '1000')

# Lägg till interaktioner
C1.add_interaction('Köpte en produkt')
C1.add_interaction('Tvättade golvet')

C2.add_interaction('Bokade ett möte')
C2.add_interaction('Mailade en fråga')

# Beräkna dagar sedan senaste interaktion
C1.calculate_days_since_last_interaction()
C2.calculate_days_since_last_interaction()
C3.calculate_days_since_last_interaction()

# NYA

# Skapar CustomerDataSystem åt bolaget Fenix AB
CRM = CustomerDataSystem('Fenix AB')

# Lägg till kunder i systemet
CRM.add_customer(C1)
CRM.add_customer(C2)
CRM.add_customer(C3)

# Lista alla kunder
CRM.list_customers()

CRM.customer_interactions('jakob@mail.com')

# Ta bort en kund baserat på e-post
CRM.remove_customer('jakob@mail.com')

# Lista kunder efter borttagning
CRM.list_customers()

# Försök ta bort en kund som inte finns
CRM.remove_customer('okand@mail.com')

# Ändra telefon
CRM.update_customer('hilmer@mail.com')

# Specifik interaktion för kund
CRM.add_specific_interaction('hilmer@mail.com', 'Hur ska jag ändra min mejladress?')

CRM.customer_interactions('hilmer@mail.com')
CRM.customer_interactions('felix@mail.com')

C1.calculate_days_since_last_interaction()