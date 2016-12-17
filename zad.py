f1 = open("plik1.txt","r+b")

for x in range(1,11):
    for y in range(1, 11):
        f1.write("%3i" %( x*y))
    f1.write("\n")

f1.seek(0)





import random

class Gracz:
    def __init__(self,kol):
        self.punkty = 0
        self.kolejnosc = kol


    def graj(self):
        roll = random.randint(-10,10)
        strzal = raw_input("podaj literke");






#f1 = open("p2.txt","wb")
#f1 = open("p1.txt","wb"),
#f1 = open("p3.txt","wb")
liczbaGraczy = int(raw_input("podaj liczbe graczy\n"))
random.seed()

a = random.randint(1,3)
if a == 1:
    plik = "p1.txt"
if a == 2:
    plik = "p2.txt"
if a == 3:
    plik = "p3.txt"


f1 = open(plik,"r+b")
f1.seek(random.randint(0,4))
haslo = ""
haslo = str(f1.readline()).upper()
haslo.replace('\n','')
print haslo.upper()
kolejnosc = range(1,liczbaGraczy+1)
gracze = range(1,liczbaGraczy+1)
while kolejnosc.__len__()>0:
    a = random.randint(0, kolejnosc.__len__()-1)
    kol = kolejnosc[a]
    kolejnosc.remove(kol)



while 1:
    for gracz in gracze:
        rzut = random.randint(-10,10)
        print "rzuca gracz " + str(gracze.index(gracz))
        if rzut == 0:
            print "BANKRUT\n"
        else:
            litera = raw_input("podaj litere\n")
            if haslo.__contains__(litera) and rzut > 0:
                gracz +=rzut

            zgadujesz = raw_input("Zgadujesz? T/N\n")
            if zgadujesz == "T":
                strzal = raw_input("podaj haslo\n")
                if haslo.__eq__(strzal):
                    print "Gracz wygral\n"
                    break
                else:
                    print "zly strzal\n"
