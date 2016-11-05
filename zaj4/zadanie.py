#napisz skrypt losujacy 6 niepotarzajacych sie liczb z zakresu od 1 do 49

import random
def zad1():
    l = range(1,49)
    random.seed()
    i =0
    while i<6:
        k = random.randint(0, 48)
        if l[k] != 0:
            print "%2i" %l[k]
            i+=1
        else:
            l[k] = 0


# ma dzialac jak gra w zgadywanie liczby: user podaje zakres liczby, maks prob,

def zad2():
    zakres = raw_input("podaj zakres?\n")
    proby = int(raw_input("podaj liczbe prob\n"))

    k = random.randint(1, int(zakres))

    while proby != 0:
        strzal = raw_input("podaj liczbe?\n")
        if strzal.isdigit():
            if(int(strzal)>k):
                print "za duzo"
            elif(int(strzal)<k):
                print "za malo"
            else:
                print "idealnie!"
                break
        proby-=1

    print "szukales %i" %k

#zad2()


#prosze napisac skrypt. dziala jak ksiazka adresowa
#dane dodajemu usowamy, modyfikujemy
#dane wyswietlane w tabeli
#

class Rekord:
    def __init__(self, i,n,t,a,k,p):
        self.imie = i
        self.nazwisko = n
        self.nrTel = t
        self.adres = a
        self.kraj = k
        self.pesel = p

class Ksiazka:
    lista = set([])

    def dodajRekord(self, a):
        self.lista.add(a)

    def usunElement(self, p):
        for x in self.lista.copy():
            if x.pesel == p:
                self.lista.remove(x)

    def wyswietl(self):
        for x in self.lista:
            print "%s  %s  %s  %s  %s  %s" % (x.imie, x.nazwisko, x.nrTel, x.adres, x.kraj, x.pesel)

    def modyfikuj(self, a1, a2, p):# wszystkie tez

        for x in self.lista:
            if x.pesel == p:
                if a1 == "imie":
                    x.imie = a2
                elif a1 == "nazwisko":
                    x.imie = a2
                elif a1 == "nrTel":
                    x.imie = a2
                elif a1 == "adres":
                    x.imie = a2
                elif a1 == "kraj":
                    x.imie = a2
                elif a1 == "pesel":
                    x.imie = a2
                break


k = Ksiazka()
while 1:
    print "\n1-dodaj rekord\n2-modyfikuj rekord\n3-usun rekord\n4-wyswietl rekord\n9-zakoncz"
    opcja = int(raw_input("podaj opcje\n"))

    if opcja == 1:
        i = raw_input("podaj imie\n")
        n = raw_input("podaj nazwisko\n")
        t = raw_input("podaj numer telefonu\n")
        a = raw_input("podaj adres\n")
        kr = raw_input("podaj kraj\n")
        p = raw_input("podaj pesel\n")

        r = Rekord(i,n,t,a,kr,p)
        k.dodajRekord(r)
    elif opcja == 2:
        a1 = raw_input("jaki parametr chcesz zmienic\n")
        a2 = raw_input("podaj nowa wartosc\n")
        pesel = raw_input("podaj PESEL\n")
        k.modyfikuj(a1,a2,pesel)
    elif opcja == 3:
        pesel = raw_input("podaj PESEL\n")
        k.usunElement(pesel)
    elif opcja == 4:
        k.wyswietl()
    elif opcja == 9:
        break
















k.wyswietl()

k.usunElement("789789")
k.wyswietl()




