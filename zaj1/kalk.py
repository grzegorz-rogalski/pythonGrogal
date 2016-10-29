
def kalkulator():
    while 1:
        print 'podaj operacje: '
        a = raw_input()
        if a.__eq__('+'):
            x = int(raw_input())
            y = int(raw_input())
            print x+y
        if a.__eq__('-'):
            x = int(raw_input())
            y = int(raw_input())
            print x-y
        if a.__eq__('*'):
            x = int(raw_input())
            y = int(raw_input())
            print x*y
        if a.__eq__('/'):
            x = int(raw_input())
            y = int(raw_input())
            print x/y
        if not a.__eq__(('+','-','*','/')):
            break
    print 'koniec'

kalkulator()
