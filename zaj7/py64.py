'''przyklad PY64. Rozne pola tekstowe'''


from Tkinter import *
from tkMessageBox import *

class EntryDemo( Frame):
    '''DEMONSTYRUJE 4 POLA TEKSTOWE'''

    def __init__(self):
        '''tworzy pakuje i binduhje zdaezenia do pol tekstowych'''
        Frame.__init__(self)
        self.pack(expand = YES, fill = BOTH)
        self.master.title("testowanie pol tekstowych")
        self.master.geometry("325x100")

        self.frame1 = Frame(self)
        self.frame1.pack(pady = 5)

        self.text1 = Entry(self.frame1, name = "tekstowe 1")
        self.text1.bind("<Return>", self.showContents)
        self.text1.pack(side = LEFT, padx = 5)

        self.text2 = Entry(self.frame1,  name="tekstowe 2")
        self.text2.insert( INSERT, "wpisz teks tutaj")
        self.text2.bind("<Return>", self.showContents)
        self.text2.pack(side=LEFT, padx=5)

        self.frame2 = Frame(self)
        self.frame2.pack(pady = 5)

        self.text3 = Entry(self.frame2, name="tekstowe 3")
        self.text3.insert(INSERT, "poel nieedytowalne")
        self.text3.config(state = DISABLED)
        self.text3.bind("<Return>", self.showContents)
        self.text3.pack(side=LEFT, padx=5)

        #tekst in [pu teks4 pojawia sie jako *
        self.text4 = Entry(self.frame2, name="tekstowe 4", show = "*")
        self.text4.insert(INSERT, "tekst ukryty")
        #self.text4.config(state=DISABLED)
        self.text4.bind("<Return>", self.showContents)
        self.text4.pack(side=LEFT, padx=5)


    def showContents(self, events):
        '''wyswietl zawartosc pola'''
        #wyswietl nazwe pola tekstowego generujaca zdarzenia
        theName = events.widget.winfo_name()
        #podsaw zawartosc tego pola do zmiennej pomnizej
        theContents = events.widget.get()
        #Po wypelnieniu pola i klikniecu ENTER zawartosc tego pola znajduje sie w theContents
        #a tu w celu szkoleniowym drukujemy w okienku
        showinfo("komunikat", theName + ": "+theContents)
def main():
    EntryDemo().mainloop()

if __name__ == "__main__":
    main()















