# Opdracht 2 lists
# Naam student: Merlijn Schaap
# Groep: IT2B


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....

rivier_info = { 
    "rijn": ["nederland", "duitsland", "frankrijk"], 
    "maas": ["nederland", "belgië", "duitsland"], 
    "nijl": ["egypte", "soedan", "oeganda"] 
}

rivieren = list(rivier_info.keys())

rivier1 = rivieren[0].capitalize()  
land1 = rivier_info[rivieren[0]][1].capitalize() 
print(f"De rivier {rivier1} stroomt onder andere door {land1}")


rivier2 = rivieren[1].capitalize()  
land2 = rivier_info[rivieren[1]][0].capitalize()  
print(f"De rivier {rivier2} stroomt onder andere door {land2}")


rivier3 = rivieren[2].capitalize() 
land3 = rivier_info[rivieren[2]][2].capitalize()  
print(f"De rivier {rivier3} stroomt onder andere door {land3}")