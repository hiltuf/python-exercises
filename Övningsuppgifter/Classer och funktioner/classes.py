class Bankkonto:
    def __init__(self, belopp):
        self.belopp = belopp 
        print(f"Start saldo: {self.belopp} kr")

    def insättning(self):
        belopp = int(input("Ange insättningsbelopp: "))
        self.belopp += belopp
        print(f"Insättning på {belopp} kr genomfört. Nytt saldo: {self.belopp} kr") 

    def uttag(self):
        belopp = int(input("Ange uttagsbelopp: "))
        if belopp <= self.belopp:
            self.belopp -= belopp
            print(f"Uttag på {belopp} kr genomfört. Nytt saldo: {self.belopp} kr")
        else:
            print("Uttaget misslyckades: otillräckligt saldo.")

    def visa_saldo(self):
        print(f"Visa saldo: {self.belopp} kr")


saldo = Bankkonto(100)

saldo.insättning()
saldo.uttag()
saldo.visa_saldo()

class Rektangel:
    def __init__(self, längd, bredd):
        self.längd = längd
        self.bredd = bredd
        print(f"Längd: {self.längd} Bredd: {self.bredd}")

    def area(self):
        arean = self.längd * self.bredd
        print(f"Arean: {arean}")

    def omkrets(self):
        omkrets = self.längd + self.längd + self.bredd + self.bredd
        print(f"Omkrets: {omkrets}")


nummer = Rektangel(50, 50)
nummer.area()
nummer.omkrets()

nummer2 = Rektangel(2, 4)
nummer2.area()
nummer2.omkrets()

class Anställd:
    def __init__(self, namn, timlön, arbetade_timmar):
        self.namn = namn
        self.timlön = timlön
        self.arbetade_timmar = arbetade_timmar
        print(f"{namn} tjänar i timmen: {timlön} kr och har arbetat {arbetade_timmar} timmar")
    def beräkna_lön(self):
        lön = self.timlön * self.arbetade_timmar
        print("Lön:", lön, "kr")

person = Anställd('Hilmer', 150, 10)
person.beräkna_lön()