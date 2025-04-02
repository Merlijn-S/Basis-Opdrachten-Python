# Opdracht 1 functies
# Naam student: Merlijn Schaap
# Groep: IT2B


def write_to_file(afile, atext):
    # je code komt hier
    # het woordje pass hieronder kun je weghalen
    pass

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)

def write_to_file(bestandsnaam, tekst):
    """
    Schrijft tekst naar een bestand. Als het bestand al bestaat, wordt de tekst toegevoegd.
    
    Args:
        bestandsnaam (str): De naam van het bestand
        tekst (str): De tekst die naar het bestand geschreven moet worden
    """
    with open(bestandsnaam, "a") as bestand:
        bestand.write(tekst + "\n")

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)