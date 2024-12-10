from datetime import *

class Customer:
    def __init__(self, name, email, phone, interactions=[], last_interaction=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.interactions = interactions
        self.last_interaction = last_interaction

    def add_interaction(self, interaction):
        self.interactions.append(interaction)
        self.last_interaction = datetime.now()  # Sätt senaste interaktionen till nuvarande tid
        print(f"Ny interaktion tillagd för {self.name}: {interaction}")
        print(f"Senaste interaktionen uppdaterad till: {self.last_interaction}\n")

    def calculate_days_since_last_interaction(self):
        if self.last_interaction is None:
            print(f"Ingen interaktion för {self.name}.\n")
            return None
        print(f"Senaste interaktionen (datum & tid) för {self.name}: {self.last_interaction}")
        print(self.last_interaction)
        days_since = (datetime.now() - self.last_interaction).days
        print(f"Senaste interaktion i dagar för {self.name}: {days_since}\n")
        return days_since
    



class CustomerDataSystem:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        while True:
            try:
                # Kontrollera om e-posten redan finns
                for existing_customer in self.customers:
                    if existing_customer.email == customer.email:
                        raise ValueError(f"En kund med mejladress {customer.email} finns redan i systemet.\n")
            
                # Om ingen duplicering hittas, lägg till kunden
                self.customers.append(customer)
                print(f"Kund {customer.name} med e-post {customer.email} har lagts till.\n")
                break  # Avsluta loopen
            except ValueError as e:
                print(e)  # Skriv ut felmeddelandet
                customer.email = input(f"Ange en annan e-postadress för {customer.name}: ")


    def remove_customer(self, email):
        # Hitta kund baserat på e-post
        try:
            customer_to_remove = None  # Variabel för att hålla den kund som ska tas bort

            # Gå igenom alla kunder och leta efter en matchning
            for customer in self.customers:
                if customer.email == email:
                    customer_to_remove = customer
                    break  # Avsluta loopen om vi hittar kunden

            # Om kunden inte finns
            if customer_to_remove is None:
                raise ValueError(f"Finns ingen kund med mejladress {email}.")
            
            # Om kunden hittades, ta bort den
            self.customers.remove(customer_to_remove)
            print(f"Kund {customer_to_remove.name} med e-post {email} har tagits bort.\n")
        
        except ValueError as e:
            print(e)
            print("Går inte att ta bort en icke existerande kund!!!\n")

    

    def update_customer(self, email):
        # Hitta kund baserat på e-post
        for customer in self.customers:
            if customer.email == email:
                print(f"Kund {customer.name} telefonnummer: {customer.phone}")
                customer.phone = input(f'Ange nya telefonnumret åt {customer.name}: ')
                print(f"Kund {customer.name} telefonnummer har ändrats till: {customer.phone}\n")
                return
        print(f"Ingen kund med e-post {email} hittades.\n")

    def add_specific_interaction(self, email, interaction):
        for customer in self.customers:
            if customer.email == email:
                customer.interactions.append(interaction)
                print(f'Kund {customer.name} har en ny interaktion: {interaction}')
                customer.last_interaction = datetime.now()
                #customer.last_interaction = datetime.now() - timedelta(days=3) #Denna kan användas för testning
                days_since = (datetime.now() - customer.last_interaction).days
                return days_since
    
    def customer_interactions(self, email):
        for customer in self.customers:
            if customer.email == email:
                if not customer.interactions:
                    print(f'Kund {customer.name} har inga interaktioner\n')
                else:
                    print(f'Kund {customer.name} interaktioner: {customer.interactions}\n')


    def list_customers(self):
        if not self.customers:
            print("Det finns inga kunder i systemet\n.")
        else:
            print("Lista över alla kunder:")
            for customer in self.customers:
                print(f"- {customer.name} telefon: {customer.phone}\n")












# Testfall
C1 = Customer('Hilmer', 'hilmer@mail.com', '073205565')
C2 = Customer('Jakob', 'jakob@mail.com', '083205262')
C3 = Customer('Felix', 'felix@mail.com', '093205212')
C4 = Customer('Samuel', 'hilmer@mail.com', '043209621')

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
CRM.add_customer(C4) #Kund med samma mejl som C1 - Hamnar i ValueError

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
C2.calculate_days_since_last_interaction()