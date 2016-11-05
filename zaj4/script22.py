'''
rekordy
'''

class Adress:
    pass

adr1 = Adress()
adr1.ulica  = 'qwerty'
adr1.nr = 13
adr1.kod = '12-556'
adr1.miasto = 'miasto'

print adr1.ulica
print adr1.__dict__