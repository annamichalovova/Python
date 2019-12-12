def reverse_ascending(seznam):
    delka = len(seznam)
    pomocny_seznam = []
    vystupni_seznam = []
    rozepsano = False
    for index in range(delka):
        if index != delka - 1 and seznam[index] < seznam[index + 1]:
            pomocny_seznam.append(seznam[index])
            rozepsano = True

        elif rozepsano:
            pomocny_seznam.append(seznam[index])
            pomocny_seznam.reverse()
            vystupni_seznam.extend(pomocny_seznam)
            pomocny_seznam.clear()
            rozepsano = False

        else:
            vystupni_seznam.append(seznam[index])
    return vystupni_seznam


vstup = [5, 7, 10, 4, 2, 7, 8, 1, 3]
print(reverse_ascending(vstup))
