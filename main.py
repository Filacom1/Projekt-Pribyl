from evidence_pojistenych import Evidence

evidence = Evidence()


#menu pro uživatele
while True:
    print("Vyberte úkon: ")
    print("1 - Přidat pojistěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojisteného")
    print("4 - Konec\n")

    akce = int(input("Číslo úkonu: \n"))

    if akce == 1:
        evidence.pridej()

    elif akce == 2:
        evidence.vypis()

    elif akce == 3:
        evidence.vyhledat()

    else:
        if akce == 4:
            evidence.konec()