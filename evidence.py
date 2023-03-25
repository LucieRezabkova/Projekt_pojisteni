from zakaznik import Zakaznik

class Evidence:
    """"
    Třída reprezentuje evidenci zákazníků.
    """

    def __init__(self):
        self.seznam_zakazniku = []
        self.operace = 0

    def novy_zakaznik(self):    # metoda pro založení nového zákazníka
        jmeno = input("Zadejte křestní jméno: \n").capitalize()
        prijmeni = input("Příjmení: \n").capitalize()
        vek = int(input("Věk: \n"))
        tel = input("Telefonní číslo: \n")
        novy_zakaznik = Zakaznik(jmeno, prijmeni, vek, tel)
        self.seznam_zakazniku.append(novy_zakaznik)
        input(f"\nZákazník {jmeno} {prijmeni} byl uložen do databáze.\nPokračujte klávesou Enter\n")

    def vypis_seznam(self):     # metoda vypíše aktální seznam zákazníků uložených v evidenci
        for zakaznik in range(len(self.seznam_zakazniku)):
            print(f"{self.seznam_zakazniku[zakaznik].jmeno}\t"
                  f"{self.seznam_zakazniku[zakaznik].prijmeni}\t"
                  f"{self.seznam_zakazniku[zakaznik].vek}\t"
                  f"{self.seznam_zakazniku[zakaznik].tel}")
        if len(self.seznam_zakazniku) < 1:
            print("Databáze neobsahuje žádné zákazníky.")
        input(f"\nPokračujte klávesou Enter\n")

    def vyhledani_zakaznika(self):      # metoda vyhledá zákazníka podle jména a příjmení
        jmeno = input("Zadejte křestní jméno hledaného zákazníka: \n").capitalize()
        prijmeni = input("Zadejte příjmení hledaného zákazníka: \n").capitalize()
        for zakaznik in self.seznam_zakazniku:
            if zakaznik.jmeno == jmeno and zakaznik.prijmeni == prijmeni:
                print(f"\n{zakaznik}")
            else:
                print("Zákazník nenalezen")
            input("\nPokračujte klávesou Enter\n")


