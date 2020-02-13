import random
# Startscherm
keuze = input("Kies een spelmode: \nA) Zelf gokken tot de max \nB) Sparren met de computer\n")
if keuze.lower == "a":
    print("Geef een code:")
if keuze.lower == "b":
    print("Gok")
def gokken():
    faker = ''
    pogingen = 0
    for x in range(4):
        temp = str(random.randint(0,2))
        faker = faker + temp
    while True:
        gok = input('Geef je 4 random getallen: ')
        if gok.isnumeric() and len(gok) == 4:
            nummer = 0
            for x in range (0,3):
                if gok[x] == faker[x]:
                    nummer += 1
            if (gok == faker):
                print('Goedzo je hebt het geraden dat nam ' + str(pogingen) + ' pogingen in beslag!')
                break
            else:
                print('Dat is niet goed, je hebt ' + str(nummer) + ' getall(en) goed geraden.')
                pogingen += 1
gokken()


