from evidence import Evidence

evidence = Evidence()

print("------------------------------\nEvidence pojištěných zákazníků\n------------------------------")

pokracovat = True
while pokracovat:
    print("1 - Přidat nového pojištěného \n"
        "2 - Vypsat všechny pojištěné \n"
        "3 - Vyhledat pojištěného \n"
        "4 - Konec \n")
    operace = input("Zvolte číslo operace: \n")

    if operace == 1:
        evidence.novy_zakaznik()
    elif operace == 2:
        evidence.vypis_seznam()
    elif operace == 3:
        evidence.vyhledani_zakaznika()
    elif operace == 4:
        print("Aplikace ukončena. Děkujeme za využití programu.")
        break
    else:
        print("Neplatná volba\n")



