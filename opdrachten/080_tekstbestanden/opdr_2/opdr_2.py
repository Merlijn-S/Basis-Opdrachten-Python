# Opdracht 2 tekstbestanden
# Naam student: Merlijn Schaap
# Groep: IT2B

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

# De rest moet jij doen.....

import random

geheim_getal = random.randint(1, 100)
aantal_pogingen = 0

while True:
    gok = int(input("Raad mijn geheime getal\n"))
    aantal_pogingen += 1
    
    if gok == geheim_getal:
        print(f"Je hebt het getal geraden het is {geheim_getal}!")
        print(f"Je hebt het in {aantal_pogingen} keer gedaan")
        break
    elif gok < geheim_getal:
        print("hoger")
    else:
        print("lager")