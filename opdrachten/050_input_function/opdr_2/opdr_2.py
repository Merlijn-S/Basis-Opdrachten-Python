# Opdracht 2 berekeningen
# Naam student: Merlijn Schaap
# Groep: IT2B

# Hier komt je code...

gasten = ["Paul", "Kees", "Marie", "Hilda"]

gasten.insert(0, "Merlijn")
print("Originele lijst:", gasten) # ["Merlijn", "Paul", "Kees", "Marie", "Hilda"]

gasten.remove("Marie")
print("Na afzegging Marie:", gasten)  # ["Merlijn", "Paul", "Kees", "Hilda"]

kees_index = gasten.index("Kees")  # Vind de positie van Kees
gasten.insert(kees_index + 1, "George")  # Voeg George toe na Kees
print("Met George erbij:", gasten)  # ["Merlijn", "Paul", "Kees", "George", "Hilda"]