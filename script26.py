
'''
operacje na plikach i katalogach
'''
'''
from os import *

#sprawdzanie w jakim katalogu jestesmy
print getcwd()

#zmiana biezacego katalogu na inny
#chdir('Test')
print getcwd()

#zawartosc katalogu
print listdir('..')

#zawartosc katalogu - sciezka absolutna
print listdir('/home/student/PycharmProjects/untitled1')

#filtrowanie plikow i katalogow wg okreslonego wzroca

import fnmatch

print fnmatch
print fnmatch.fnmatch('Python', 'P*n')
print fnmatch.fnmatch('Python', 'P*e')

#lista plikow z rozrzeszeniem .py
print [x for x in listdir(r'/home/student/PycharmProjects/untitled1')
       if fnmatch.fnmatch(x,'*.py')]

print [x for x in listdir(r'/home/student/PycharmProjects/untitled1')
       if fnmatch.fnmatch(x,'*[61].*')]

import glob
for x in glob.glob(r'/home/student/PycharmProjects/untitled1/*[61].*'):
    print x

#rozdzielenie scioezki absolutnej w katalog w ktorym znajduje sie plik oraz nazwa pliku
print path.split('/home/student/PycharmProjects/untitled1/script21.py')

for x in glob.glob(r'../*[61].*'):
    print path.split(x)[1]

#laczenie ciagow katalogow w sciezke
print path.join('/','home','student','PycharmProjects','untitled1','script21.py')
print path.join(r'/home/student','PycharmProjects','untitled1','script21.py')

#sprawdzanie czy pofdana sciezka jest ab solutna
print path.isabs(r'../script21.py')
print path.isabs(r'/home/student/PycharmProjects/untitled1/script21.py')

##sprawdzanie czy obiekt dyskowy istnieje
print path.exists('/home/student/PycharmProjects/untitled1/script21.py')
print path.exists('/home/student/PycharmProjects/untitled1')

#zmieniamy nazwy katalogu lub pliku
#rename('../Test','../NTEST')
print path.exists('NTEST')
print listdir('.')

#sprawdzanie czy dany obiekt dyskowy jest plikem
print path.isfile('NTEST')
print path.isfile('script25.py')

#sprawdzanie czy obiekt jest katalofgiem
print path.isdir('NTEST')
print path.isdir('script25.py')

#sprawdzanue czy dany obiekt jest dyskiem
print path.ismount('NTEST')
print path.ismount('/home')

#sprawdzanie dlugosci pliku
#print path.getsize('NTEST')
print path.getsize('script25.py')

for x in listdir('.'):
    print x, path.getsize(x)


#czas stworzonego pliku
from time import ctime
print ctime(path.getctime('script25.py'))

#czas ostatniej modyfikacji
print ctime(path.getmtime('script25.py'))

#rekursywne przechodzenie katalogow
for sciezka, katalogi, pliki in walk(r'./'):
    print 'W katalogu %s znajduje sie %i bajtow w %i plikach' \
        %(sciezka,sum(path.getsize(path.join(sciezka,nazwa))
                      for nazwa in pliki), len(pliki))

'''

'''
napisz skrypt ktory
1 user podaje sciezke do folderu
2 wyswietlone info: ilsoc plikow, rozmiar plikow, ilsoc folderow, rozmiar folderow, rozmiar folderu w ktorym
jestes(przlicz na kilobajty i megabnajty)
'''
from os import *

a = raw_input('podaj sciezke')
katalogi = 0
pliki = 0
rozmiaryPlikow = 0.0
rozmiaryfolderow = 0.0
rozmiar = 0.0
tabRozmiaryPlikow = []
tabRozmiaryfolderow = []

for x in listdir(a):

    if path.isdir(x):
        katalogi += 1
        rozmiaryfolderow += path.getsize(x)
        print 'mamy katalog %s o wielkosci %i b %f kb %f MB' %(
            str(x), path.getsize(x),float(path.getsize(x))/1024.0,float(path.getsize(x))/(1024*1024))
        #rozmiaryfolderow.append(path.getsize(x))
    if path.isfile(x):
        pliki += 1
        rozmiaryPlikow += path.getsize(x)
        print 'mamy plik  %s o wielkosci %i b %f kb %f MB' % (
             str(x), path.getsize(x), float(path.getsize(x)) / 1024, float(path.getsize(x)) / (1024 * 1024))
        #rozmiaryPlikow.append(path.getsize(x))

    rozmiar += path.getsize(x)

#print 'rozmiary pliow' + tabRozmiaryPlikow
#print 'rozmiary folderow' + tabRozmiaryfolderow
print '\n mamy %i plikow o rozmarze %i b %f kb %f MB\n mamy %i folderow o rozmarze %i b %f kb %f MB\n a calosc wazy %i b %f kb %f MB' \
    %(pliki,rozmiaryPlikow,rozmiaryPlikow/1024,rozmiaryPlikow/(1024*1024),
        katalogi,rozmiaryfolderow,rozmiaryfolderow/1024.0,rozmiaryfolderow/(1024*1024),
        rozmiar,rozmiar/1024,rozmiar/(1024*1024))




