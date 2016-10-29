#napisz skrypt ktory znajdzie i wyswietli wystapienie 1 miejsca wystapienia liczby w liscie

l = range(1,21)
#print l
#print l[l.index(5)]

#napisz skrypt ktory wylicza najwieszy wspolny dzielnik i najwieksza wpoilna wielokrotbnoisc

def NWD(a,b):
    while b!=0:
        c=a % b
        a=b
        b=c
    return a

def NWW(a,b):
    c = a*b/NWD(a,b)
    return c

#print NWD(192,348)
#print NWW(20,30)

#sito eratostenesa(czas 2 tyg)
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
        b = raw_input("Podaj zakres\n")
        if b > 0 & b.isdigit():
            a.sitko(int(b))
            a.wyswietl()
            break

fun()