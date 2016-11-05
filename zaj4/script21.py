'''
moduly
'''
import random
#from random import *
#from random import randint

random.seed()
print random.randint(1,15) #losuje liczbe z zakresu
print random.randint(1,15)

l = range(1,10)
print random.choice(l)# wybier losowy element

random.shuffle(l) #losowa permutrajca
print l

print random.random()#liczba losowa z przedzialo 0 do 1

print random.uniform(10,30) #losowa liczbna rzczywista z podanego przedzialu

print random.normalvariate(4,48)  #zmienna losowa o rozkladznie normalnym o sredniwej 5 i o rozkladzie

