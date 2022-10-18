#Vytváří pojištěnce s jeho údaji
class Pojistenec:
    

    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon
    
    #Vrací textovou podobu pojištěnce
    def __str__ (self):
        return f"{self.jmeno}\t{self.prijmeni}\t{self.vek}\t{self.telefon}"


