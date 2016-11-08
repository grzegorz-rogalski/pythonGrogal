#prosze napisac skrypt. dziala jak ksiazka adresowa
#dane dodajemu usowamy, modyfikujemy
#dane wyswietlane w tabeli

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
                return 1
        return 0

    def wyswietl(self):
        for x in self.lista:
            print "%s  %s  %s  %s  %s  %s" % (x.imie, x.nazwisko, x.nrTel, x.adres, x.kraj, x.pesel)

    def modyfikuj(self, a1, a2, p):
        for x in self.lista:
            if x.pesel == p:
                if a1 == "imie":
                    x.imie = a2
                elif a1 == "nazwisko":
                    x.nazwisko = a2
                elif a1 == "nrTel":
                    x.nrTel = a2
                elif a1 == "adres":
                    x.adres = a2
                elif a1 == "kraj":
                    x.kraj = a2
                elif a1 == "pesel":
                    x.pesel = a2
                break

    def modyfikujCalyRekord(self, p, r):
        if self.usunElement(self, p) == 1:
            self.dodajRekord(self, r)
        else:
            print "podano niprawidlowy PESEL\n"


def nowyRekord():
    i = raw_input("podaj imie\n")
    n = raw_input("podaj nazwisko\n")
    t = raw_input("podaj numer telefonu\n")
    a = raw_input("podaj adres\n")
    kr = raw_input("podaj kraj\n")
    p = raw_input("podaj pesel\n")

    r = Rekord(i, n, t, a, kr, p)
    return r

k = Ksiazka()
while 1:
    print "\n1-dodaj rekord\n2-modyfikuj rekord\n3-usun rekord\n4-wyswietl rekord\n9-zakoncz"
    opcja = raw_input("podaj opcje\n")
    if opcja.isdigit():
        opcja = int(opcja)
        if opcja == 1:
            k.dodajRekord(nowyRekord())
        elif opcja == 2:
            opcja2 = raw_input("1-modyfikuj caly rekord\n2-pojedynczy parametr\n")
            if opcja2.isdigit():
                opcja2 = int(opcja2)
                if opcja2 == 1:
                    pesel = raw_input("podaj PESEL\n")
                    if k.usunElement(pesel) == 0:
                        print 'podano nieprawidlowy PESEL\n'
                    else:
                        k.dodajRekord(nowyRekord())
                elif opcja2 == 2:
                    a1 = raw_input("jaki parametr chcesz zmienic\n")
                    a2 = raw_input("podaj nowa wartosc\n")
                    pesel = raw_input("podaj PESEL\n")
                    k.modyfikuj(a1, a2, pesel)
        elif opcja == 3:
            pesel = raw_input("podaj PESEL\n")
            if k.usunElement(pesel) == 0:
                print 'podano nieprawidlowy PESEL\n'
        elif opcja == 4:
            k.wyswietl()
        elif opcja == 9:
            break