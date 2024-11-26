from datetime import datetime

class Customer:
    def __init__(self, name, email, phone, interactions=None, last_interaction=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.interactions = interactions if interactions is not None else []  # En lista över alla interaktioner
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
        days_since = (datetime.now() - self.last_interaction).days
        print(f"Senaste interaktion i dagar för: {self.name}: {days_since}")
        return days_since

# Testfall
customer1 = Customer('Hilmer', 'hillefifa@gmail.com', '3000')
customer2 = Customer('Jakob', 'jakob@mail.com', '2000')
customer3 = Customer('Felix', 'felix@mail.com', '1000')

# Lägg till interaktioner
customer1.add_interaction('Köpte en produkt')
customer1.add_interaction('Tvättade golvet')

customer2.add_interaction('Bokade ett möte')
customer2.add_interaction('Mailade en fråga')

# Beräkna dagar sedan senaste interaktion
customer1.calculate_days_since_last_interaction()
customer2.calculate_days_since_last_interaction()
customer3.calculate_days_since_last_interaction()
