# Opdracht 1 condities
# Naam student: Merlijn Schaap
# Groep: IT2B

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

getallen = []

for i in range(1, 11):
    getallen.append(i)

grote_getallen = [getal for getal in getallen if getal > 4]

print(grote_getallen)