import random
# Startscherm
keuze = input("Kies een spelmode: \nA) Zelf gokken tot de max \nB) Sparren met de computer\n")
if keuze.lower == "a":          # als de user op a drukt dan gaat het naar de computer.
    print("Geef een code:")
if keuze.lower == "b":          # als de user b drukt dan doet de mens het werk.
    print("Gok")
def gokken():
    string = ''                      # een lege string om de input later op te slaan
    pogingen = 0
    for x in range(4):                  # het aantal maximale range om te gokken
        temp = str(random.randrange(0,4))
        string = string + temp                    # for elke string wordt het opgeslagen
    while True:
        gok = input('Geef je 4 random getallen: ')
        if gok.isnumeric() and len(gok) == 4:      # dus als de input gelijk is aan een integer en de lengte van de string is gelijk aan 4 dan verder
            nummer = 0                          # de index 0
            for x in range (0,3):
                if gok[x] == string[x]:      # eerste index controleren of het juist is of niet en dan verder
                    nummer += 1
            if (gok == string):          # geeft aan in hoevel stappen het geraden is en het aantal stappen
                print('Goedzo je hebt het geraden dat nam ' + str(pogingen) + ' pogingen in beslag!')
                break
            else:                   #  geeft aan dat het het niet klopt en/of hoeveel getallen juist zijn.
                print('Dat is niet goed, je hebt ' + str(nummer) + ' getall(en) goed geraden.')
                pogingen += 1
gokken()


