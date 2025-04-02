# Opdracht 1 input function
# Naam student: Merlijn Schaap
# Groep: IT2B

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

import math

def pythag (a, b)
        sum_of_squares = a * a + b * b
        c = math.sqrt(sum_of_squares)

        return c

solution = pythag(4, 3)

print(solution)