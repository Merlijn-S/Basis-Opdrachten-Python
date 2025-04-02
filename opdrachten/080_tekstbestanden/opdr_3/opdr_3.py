# Opdracht 3 Tekst opslaan
# Naam student: Merlijn Schaap
# Groep: IT2B

def encrypt_tekst(tekst):
    versleutelde_tekst = ""
    
    for letter in tekst:
        if letter.isalpha():
            is_hoofdletter = letter.isupper()
            code = ord(letter.lower())
            nieuwe_code = code + 5
            if nieuwe_code > ord('z'):
                nieuwe_code -= 26
            nieuwe_letter = chr(nieuwe_code)
            if is_hoofdletter:
                nieuwe_letter = nieuwe_letter.upper()
            versleutelde_tekst += nieuwe_letter
        else:
            versleutelde_tekst += letter
            
    return versleutelde_tekst

invoer = input("Geef de tekst die wilt encrypten..\n")

resultaat = encrypt_tekst(invoer)
print(resultaat)

