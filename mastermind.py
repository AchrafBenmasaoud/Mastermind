from wit import raden
import random

def gokkentjes():
    string = ''  # een lege string om de input later op te slaan
    for x in range(0, 4):  # het aantal maximale range om te gokken
        temp = str(random.randrange(0, 4))
        string = string + temp  # for elke string wordt het opgeslagen
        print(string)
    while True:
        gok = input('Geef je 4 random getallen: ')
        pogingen = 1  # dus als de input gelijk is aan een integer en de lengte van de string is gelijk aan 4 dan verder
        zwart = 0
        wit = 0
        if gok.isnumeric() and len(gok) == 4:
            for x in range(0, 4):
                if gok[x] == string[x]:  # eerste index controleren of het juist is of niet en dan verder
                    zwart += 1
                elif gok[x] in string and gok[x] != string[x]:
                    wit += 1
            if (gok == string):  # geeft aan in hoevel stappen het geraden is en het aantal stappen
                print('Mastermind! je hebt het geraden binnen ' + str(pogingen) + ' pogingen! ')
            else:  # geeft aan dat het het niet klopt en/of hoeveel zwarte en/of witte je hebt geraden
                print('je hebt nu ' + str(zwart) + ' zwarte geraden')
                print('Je hebt nu ' + str(wit) + ' witte geraden')
            pogingen += 1
        elif gok != len(gok):
            print('Onjuiste waarde')


def algoritme1():
    pogingen = 0
    geheim = input('Geef je 4 random getallen tussen de 0-5 ')
    geheime_lijst = [int(x) for x in geheim]
    lijst=[]
    for i in range(0, 6):
        for j in range(0, 6):
             for k in range(0, 6):
                for l in range(0, 6):
                    lijst.append([i,j,k,l])
    new_list = lijst[:]
    for x in lijst:
        pogingen += 1
        a = random.choice(lijst)
        mogelijkheid =raden(a, geheime_lijst)
        checken = raden(x, geheime_lijst)
        if checken != mogelijkheid:
            new_list.remove(x)
            print(a)
            continue
        elif lijst != 1:
            print('Computer heeft de code geraden ik ben je te slim af :))')
            print('Computer Heeft het geraden binnen: ' + str(pogingen) + ' pogingen. ')
            break
    if pogingen <= 10:
        print('Computer is de nieuwe mastermind! ')
    elif pogingen > 10:
        print('Computer heeft zijn dag niet ')

def algoritme2:






def eigenalgoritme3:




def startscherm():
    print('''                            [---Welkom bij het spel Mastermind---]

1) Als je voor de optie A kiest ben je of bang voor de computer, of je mag van je vrouw niet meer naar de casino.
2) Als je voor optie B kiest dan ga je de ring in met de computer en op hoop van zegen dat je wint.
            ''')
    keuze = input(
        'Na de mooie uitleg mag je nu kiezen van wat je wil: \nA) Zelf lekker gokken. \nB) Sparren met de computer.\n')
    if keuze == 'a':
        gokkentjes()
    elif keuze == 'b':
        algoritme1()
startscherm()
