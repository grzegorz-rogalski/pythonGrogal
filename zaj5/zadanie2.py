from random import *


class klasa:
    lista, l1,l2,l3, ln= [],[],[],[],[]
    seed(12)
    def a(self):
        a = 20#int(raw_input("podaj n"))
        self.lista = range(a)

    def b(self):

        a = 1#int(raw_input("podaj a"))
        b = 15#int(raw_input("podaj b"))
        x=0
        while x < self.lista.__len__():
            self.lista[x] = randint(a,b)
            x+=1

    def c(self):
        print self.lista

    def d(self):
        self.l1 = [x for x in self.lista if x % 2]
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
        duplikaty = []
        duplikaty = list(set(self.lista))
        for x in duplikaty:
            self.lista[self.lista.index(x)] = "X"

    def g(self):
        duplikaty = []
        duplikaty = list(set(self.lista))
        for x in duplikaty:
            self.lista.remove(x)

    def h(self):
        print reduce(lambda x, y: (x + y)/self.lista.__len__(), self.lista)
        print [x*x for x in self.lista]

    def i(self):
        for x in self.l1:
            if self.lista.__contains__(x):
                self.lista[self.lista.index(x)] = "A"
        for x in self.l2:
            if self.lista.__contains__(x):
                self.lista[self.lista.index(x)] = "E"
        for x in self.l3:
            if self.lista.__contains__(x):
                self.lista[self.lista.index(x)] = "L"

    def j(self):
        n = 100
        l = range(1, n + 1)
        i = 2
        while i < n ** 0.5:
            if l[i] != 0:
                j = i * i
                while j < n:
                    l[j] = 0
                    j += i
            i = i + 1
        k = []
        for x in l:
            if x != 0 and l.index(x) != 0 and l.index(x) != 1:
                k.append(l.index(x))

        for x in k:
            if self.lista.__contains__(x):
                self.lista[self.lista.index(x)] = "L"

    def k(self):
        k =[]
        k = [x for x in self.lista if not isinstance(x, basestring)]



a = klasa()
a.a()
a.b()
a.c()
a.d()
a.e()
a.i()
a.j()
a.k()