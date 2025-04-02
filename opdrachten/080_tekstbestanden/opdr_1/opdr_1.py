# Opdracht 1 while-loops
# Naam student: Merlijn Schaap
# Groep: IT2B

# Jouw code komt hier

vragen = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind jij de mooiste stad van Nederland?"
]

antwoorden = []

for vraag in vragen:
    antwoord = input(vraag + "\n")
    antwoorden.append(antwoord)

with open("enquete_resultaten.txt", "w") as bestand:
    for i, (vraag, antwoord) in enumerate(zip(vragen, antwoorden), 1):
        bestand.write(f"Vraag {i}: {vraag}\n")
        bestand.write(f"Antwoord: {antwoord}\n")
        bestand.write("-" * 30 + "\n")

print("Bedankt voor het invullen! De antwoorden zijn opgeslagen in enquete_resultaten.txt")