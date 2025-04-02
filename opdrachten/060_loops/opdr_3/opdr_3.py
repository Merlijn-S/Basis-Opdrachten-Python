# Opdracht 3 input functie
# Naam student: Merlijn Schaap
# Groep: IT2B

# Hier komt je code...

# Hier start de for-loop

resultaten = []

for i in range(3, 82, 3):  # 82 omdat range exclusief is aan de bovenkant
    resultaat = (i ** 2) / 3
    resultaten.append(resultaat)

print(resultaten)