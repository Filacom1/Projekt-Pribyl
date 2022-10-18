from pojistenec import Pojistenec
#Třída slouží pro evidenci pojištěných
class Evidence:
    databaze_pojistencu = []

    
    def __init__(self):
        pass

        # Metoda vytvoří instanci pojištěnce a přidá ho s jeho údaji do seznamu 
    def pridej(self):
        novy_pojistenec = Pojistenec(input("Jméno: "), input("Příjmení: "), input("Věk: "), input("Telefon: "))
        self.databaze_pojistencu.append(novy_pojistenec)
        print("Pojištěnec byl přidán do evidence")

        # Metoda vypíše všechny vložené pojištěnce ze seznamu
    def vypis(self):
        for pojistenec in self.databaze_pojistencu:
            print(pojistenec)

        # Metoda vyhledá a vypíše pojištěnce podle jména a příjmení

    def vyhledat(self):
        hledane_jmeno = input("Zadejte hledané jméno: ")
        hledane_prijmeni = input("Zadejete hůedané příjmení: ")
        for pojistenec in self.databaze_pojistencu:
            if hledane_jmeno == pojistenec.jmeno and hledane_prijmeni == pojistenec.prijmeni:
                print(f"{pojistenec}\n")
                
            elif hledane_jmeno != pojistenec.jmeno and hledane_prijmeni != pojistenec.prijmeni:
                print("\nJméno a příjmení nenalezeno!!!\n")
                

        # Metdoda ukončí program
    def konec(self):
        print(input("Pro ukončení programu stiskněte libovolnou klávesu.."))
        input()
        


