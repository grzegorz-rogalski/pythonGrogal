# -*- coding: utf-8 -*-

'''f1 = open("plik1.txt","r+b")

for x in range(1,11):
    for y in range(1, 11):
        f1.write("%3i" %( x*y))
    f1.write("\n")

f1.seek(0)
'''

'''
Napisać skrypt, który będzie działał jak gra w koło fortuny. Na początku gry podaje się
liczbę uczestników oraz losowo wybierana jest kategoria i hasło z pliku txt. Następnie każdy
z uczestników losuje liczbę od 1 do ilości uczestników. W ten sposób ustala się kolejność
gry przy pierwszym kręceniu kołem. Na kole znajdują się cyfry od -10 do 10. Liczby te
symbolizują pkt. Użytkownik kręci kołem czyli losuje liczbę. Liczba 0 symbolizuje
bankruta i kolejny uczestnik losuje. Następnie podaje literkę. Jeśli literka znajduje się w
haśle i pkt są ujemne to nie otrzymuje ich. W przypadku pkt dodatnich są dodawane do
sumy pkt. Uczestnik po wylosowaniu literki ma prawo do odgadnięcia hasła. Jeśli zgadnie
jego pkt są mnożone przez ilość literek, które nie zostały odkryte. Po odgadnięciu hasła pkt
wszystkich uczestników zapisywane są do pliku txt.
'''


import random

class Gra:
    def graj(self):
        # f1 = open("p2.txt","wb")
        # f1 = open("p1.txt","wb"),
        # f1 = open("p3.txt","wb")
        liczbaGraczy = int(raw_input("podaj liczbe graczy\n"))
        random.seed()

        a = random.randint(1, 3)
        if a == 1:
            plik = "p1.txt"
        if a == 2:
            plik = "p2.txt"
        if a == 3:
            plik = "p3.txt"

        f1 = open(plik, "r+b")
        f1.seek(random.randint(0, 4))
        haslo = ""
        haslo = str(f1.readline()).upper()
        haslo.replace('\n', '')
        print haslo.upper()
        kolejnosc = range(1, liczbaGraczy + 1)
        gracze = range(1, liczbaGraczy + 1)
        while kolejnosc.__len__() > 0:
            a = random.randint(0, kolejnosc.__len__() - 1)
            kol = kolejnosc[a]
            kolejnosc.remove(kol)

        output = []
        for a in haslo:
            if a == ' ':
                output.append(' ')
            else:
                output.append('_')

        while 1:
            for gracz in gracze:
                print output
                rzut = random.randint(-10, 10)
                print "rzuca gracz " + str(gracze.index(gracz))
                if rzut == 0:
                    print "BANKRUT\n"
                else:
                    litera = raw_input("podaj litere\n")
                    if haslo.__contains__(litera) and rzut > 0:
                        gracz += rzut
                        i = 0
                        while i < haslo.__len__():
                            if litera == x:
                                output[haslo.index(x)] = litera

                    zgadujesz = raw_input("Zgadujesz? T/N\n")
                    if zgadujesz == "T":
                        strzal = raw_input("podaj haslo\n")
                        if haslo.__eq__(strzal):
                            print "Gracz wygral\n"
                            break
                        else:
                            print "zly strzal\n"

        print gracze

a = Gra()
a.graj()