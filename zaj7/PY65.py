'''przyklad radiobutton'''
from Tkinter import *
root = Tk()
root.title(u"wykszta\u0142cenie")

var = IntVar()
for text, value in [('Podstawowe', 1), (u'Niepe\u0142ne \u015brednie', 2), (u'\015arednie', 3),
                    (u'Niepe\u0142ne wy\u017csze', 4), (u'Wy\u017csze',5), ('brak danych', 6)]:
    Radiobutton(root,text = text, value = value, variable = var).pack(anchor = W)

var.set(3)
root.geometry("250x150")
root,mainloop()
print var.get()