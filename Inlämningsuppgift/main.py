from datetime import *

class Customer:
    def __init__(self, name, email, phone, interactions=None, last_interaction=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.interactions = interactions if interactions is not None else []
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
        days_since = (datetime.now() - self.last_interaction).days
        print(f"Senaste interaktion i dagar för {self.name}: {days_since}\n")
        #print(f"Senaste interaktion i dagar för {self.name}: {self.inactive_days_return()}\n") # Bevisning att inactive days för uppdatera i dagar för kunden
        return days_since
    
    def inactive_days_return(self):
        if not self.last_interaction:
            return None
        return (datetime.now() - self.last_interaction).days #Denna beräknar i Realtid terminal
        #return 31 # Denna har jag för att visa att dagarna faktiskt räknas i inaktiva kunder printen

class CustomerDataSystem:
    def __init__(self, name):
        self.name = name
        self.customers = []
        print(f"----CustomerDataSystem åt {name}----\n")

    def add_customer(self, customer):
        while True:
            try:
                # Kontrollera om e-posten redan finns
                for existing_customer in self.customers:
                    if existing_customer.email == customer.email:
                        raise ValueError(f"\nEn kund med mejladress {customer.email} finns redan i systemet.\n")
            
                # Om ingen duplicering hittas, lägg till kunden
                self.customers.append(customer)
                print(f"Kund {customer.name} med e-post {customer.email} har lagts till.")
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
                raise ValueError(f"\nFinns ingen kund med mejladress {email}.")
            
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
        try:
            for customer in self.customers:
                if customer.email == email:
                    # Lägg till interaktionen och uppdatera senaste interaktionen
                    customer.interactions.append(interaction)
                    customer.last_interaction = datetime.now()  # Uppdatera senaste interaktionstidpunkt

                    # Beräkna och returnera antalet dagar sedan senaste interaktionen
                    days_since = customer.inactive_days_return()
                    #customer.last_interaction = datetime.now() - timedelta(days=30) #Denna kan användas för testning
                    print(f'Kund {customer.name} har en ny interaktion: {interaction} Antal dagar sedan senaste interaktion: {days_since}\n')
                    return days_since  # Returnera antalet dagar sedan senaste interaktionen
                
            # Om vi inte hittar kunden med e-posten, kasta ett undantag
            raise ValueError(f"Kunden med e-post {email} finns INTE i systemet och kan därmed inte skapa ett ärende!\n")
        except ValueError as e:
            # Fångar undantaget och skriver ut felmeddelandet
            print(e)
    
    def inactive_user(self):
        inactive_customers = []
        active_customers = []
        for customer in self.customers:
            days_since = customer.inactive_days_return()
            if days_since is not None and days_since > 30:
                inactive_customers.append(f"{customer.name} är inaktiv. {days_since} dagar sedan senaste interaktion.")
            else:
                active_customers.append(f"{customer.name} är aktiv eller har ingen interaktion registrerad. {days_since}")
        
        if inactive_customers:
            print("\nInaktiva kunder:")
            for customer in inactive_customers:
                print(customer)
        else:
            print("Inga inaktiva kunder hittades.\n")

        if active_customers:
            print("\nAktiva kunder:")
            for customer in active_customers:
                print(customer)

    
    def customer_interactions(self, email):
        # Söker efter kunden baserat på e-post
        for customer in self.customers:
            if customer.email == email:
                if not customer.interactions:
                    print(f'Kund {customer.name} har inga interaktioner.\n')
                else:
                    print(f'\nKund {customer.name} interaktioner: {customer.interactions}') #Printar kundens alla interaktioner
                    print(f'Kund {customer.name} senaste interaktion: {customer.interactions[-1]}\n') #Printar kundens senaste interaktion
                return  # Avsluta när kunden hittas
        print(f"Ingen kund med e-post {email} hittades och därmed inga interaktioner.\n")  # Om kunden inte finns


    def list_customers(self):
        if not self.customers:
            print("Det finns inga kunder i systemet\n.")
        else:
            print("\nLista över alla kunder:")
            for customer in self.customers:
                print(f"- Namn: {customer.name}, Email: {customer.email}, Telefon: {customer.phone}")












# Testfall
C1 = Customer('Hilmer Tufvasson', 'hilmer@mail.com', '073205565')
C2 = Customer('Jakob Höglund', 'jakob@mail.com', '083205262')
C3 = Customer('Felix Torsten', 'felix@mail.com', '093205212')
C4 = Customer('Samuel Donter', 'hilmer@mail.com', '043209621')

# Lägg till interaktioner
C1.add_interaction('Köpte en produkt')
C1.add_interaction('Tvättade golvet')

C2.add_interaction('Bokade ett möte')
C2.add_interaction('Mailade en fråga')

#C3.add_interaction('Buuhoooo') #Lägg till för att visa

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
CRM.remove_customer('okand@mail.com') #Value Error

# Ändra telefonnummer
CRM.update_customer('hilmer@mail.com')

# Specifik interaktion för kund
CRM.add_specific_interaction('hilmer@mail.com', 'Hur ska jag ändra min mejladress?')
CRM.add_specific_interaction('gustav@mail.com', 'Jag kan inte skapa ett ärende för jag finns inte i systemet!')

CRM.customer_interactions('hilmer@mail.com')
CRM.customer_interactions('felix@mail.com')
CRM.customer_interactions('jakob@mail.com')


C1.calculate_days_since_last_interaction()

CRM.inactive_user()