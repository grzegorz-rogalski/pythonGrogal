'''
ciag fiab
'''

def ciagF(n):

    t = [0,1]
    tab = t+range(2,n+1)
    print tab
    if n == 0:
        print 0
    if n== 1:
        print 1
    else:
        print "0\n1"
        for x in range(2, n):
            tab[x] = tab[x-1]+tab[x-2]
            print tab[x]

ciagF(21)