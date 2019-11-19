def pigeon(wheat):
    pigeons, increment, fed = 0, 0, 0
    while wheat>fed:
        increment += 1
        pigeons += increment 
        fed = min(pigeons,wheat)
        wheat -= pigeons
    return fed

wheat = int(input("Zadej číslo:   "))
print("The number of fed pigeons as an integeris",pigeon(wheat))
