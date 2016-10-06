'''
Listy - modyfikacje
'''

lista = [1,2,3]
lista2 = lista+[4,5,6]
print lista2

lista = [4,6,2,4,8]
lista.sort()
print lista
lista.reverse()
print lista

lista.append(6)
print lista

lista.insert(2,10)
print lista

lista.pop()
print lista

lista.remove(4)
print lista

del lista[1:3]
print lista