# Opdracht 1 functies
# Naam student: Merlijn Schaap
# Groep: IT2B

def kilometers_naar_miles(kilometers):
    """
    Converteert kilometers naar miles (1 mile = 1.609344 km)
    
    Args:
        kilometers (float): Aantal kilometers om te converteren
        
    Returns:
        float: Het equivalente aantal miles
    """
    return kilometers / 1.609344

def miles_naar_kilometers(miles):
    """
    Converteert miles naar kilometers (1 mile = 1.609344 km)
    
    Args:
        miles (float): Aantal miles om te converteren
        
    Returns:
        float: Het equivalente aantal kilometers
    """
    return miles * 1.609344

kilometers = 1223
miles = 867

miles_resultaat = kilometers_naar_miles(kilometers)
km_resultaat = miles_naar_kilometers(miles)

print(f"{kilometers} kilometers = {miles_resultaat} miles")
print(f"{miles} miles = {km_resultaat} kilometers")