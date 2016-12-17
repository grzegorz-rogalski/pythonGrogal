from random import *


class klasa:
    lista, l1,l2,l3, ln= [],[],[],[],[]
    def a(self):
        a = 20#int(raw_input("podaj n"))
        self.lista = range(a)

    def b(self):
        seed(12)
        a = 1#int(raw_input("podaj a"))
        b = 15#int(raw_input("podaj b"))
        x=0
        while x < self.lista.__len__():
            self.lista[x] = randint(a,b)
            x+=1

    def c(self):
        print self.lista

    def d(self):
        self.l1 = [x for x in self.lista if x % 2 ]
        self.l2 = [x for x in self.lista if x % 3]
        self.l3 = [x for x in self.lista if x % 5]

    def e(self):
        q = []
        q += list(set(self.l1))
        q += list(set(self.l2))
        q += list(set(self.l3))
        self.ln = list(set(q))
        print self.ln

    def f(self):
        dz = lambda x: self.ln.__contains__(x)

        self.l1 = [x for x in self.l1 if self.ln.__contains__(x)]
        for x in self.l1:
            if dz(x):
                self.l1.remove(x)
        print self.l1

a = klasa()
a.a()
a.b()
a.c()
a.d()
a.e()
a.f()