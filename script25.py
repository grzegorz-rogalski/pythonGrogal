# -*- coding: utf-8 -*-
'''
pliki
'''

#utworzenie i otwarcie do zpaisu pliku
f1 = open("plik1.txt","wb")

#3 podstawowe atrybuty obiektow plikowych

#name - nazwa
print f1.name

#mode - okresl tryb w jakim otworzono plik
print f1.mode

#closed - okreslenie czy plik jest zamkniety
print f1.closed

#metody obslugi plikow

#metody do obslugi pliku

#write - zapisuje
f1.write("pierwszy plik")

#flush zapisuej dane z bifora do pliku(przydatne w Windows)
f1.flush()

#close - zapisuje dane z bufora do pliku zi zamuka plik
f1.close()

#otwacie pliku do modyfikacji
f1 = open("plik1.txt", "r+b")

#read odczytuje z pliuku napis
print f1.read()

#tell - podaje aktyualna pozycje plilku
print f1.tell()

#seek ustawia pozycje w pliku na podana
f1.seek(0)

#napisanie poczatki\u pliuk
f1.write("asdasdasd")

#przesuniecie na wzgledna pozycje pliku(od aktualnej pozycji)
f1.seek(-9,1)

#wczytanie fragmentu zawartosci o okreslonej dlugosci
print f1.read(14)

#writelines - zapisuje do plikow sekwence napisow (bez dodawani aautomacztynie separatorow
f1.writelines(["\nn3 linia","\nn4 linia","\nn5 linia"])

#readlines wczutuje z pliku sekwencje napsow
f1.seek(0)
print f1.readlines()

#truncate - skraca plik na [pdanejk pozycji
f1.truncate(30)
f1.seek(0)
print f1.read()

#issaty - zwraca true jezeli plik jest doplaczony do urzadzenia terminalowego
print f1.isatty()

# przyklad strumienia stdin out
import sys
print sys.stdout.isatty()

#przyklad przkierowania wewnatrz programu
import sys
ekran = sys.stdout
sys.stdout = open("wejscie.txt","w")
print "jestem tutaj"
print "gdzie ty poszedles"
sys.__stdout__ = ekran
print open("wejscie.txt","r").read()

