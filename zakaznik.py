class Zakaznik:
    """
    Třída reprezentuje nového zákaznika.
    """
    def __init__(self, jmeno, prijmeni, vek, tel):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel = tel

    def __str__(self):
        return f"{self.jmeno}\t{self.prijmeni}\t{self.vek}\t{self.tel}"
