class Sito:

    def sitko(self, n):
        l = range(1,n+1)
        i = 2
        while i < n**0.5:
            if l[i] != 0:
                j = i * i
                while  j< n:
                    l[j]=0
                    j+=i
            i = i+1
        k = []
        for x in l:
            if x != 0:
                k.append(l.index(x))
        self.lista = k

    def wyswietl(self):
        print self.lista


def fun():
    a = Sito()
    while 1:
        b = raw_input("Podaj zakres, aby zakończyć wpisz: koniec\n")
        if (b > 0) and (b.isdigit()):
            a.sitko(int(b))
            a.wyswietl()
            break
        if b.lower() == "koniec":
            break

fun()