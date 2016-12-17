#konweter

from Tkinter import *
from tkMessageBox import *


class EntryDemo( Frame):
    def __init__(self):
        '''tworzy pakuje i binduhje zdaezenia do pol tekstowych'''
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("testowanie pol tekstowych")
        self.master.geometry("325x100")




        self.frame2 = Frame(self)
        self.frame2.pack(pady=5)

        self.text2 = Entry(self.frame2, name="tekstowe 2")
        self.text2.insert(INSERT, "wpisz teks tutaj")
        self.text2.bind("<Return>", self.showContents)
        self.text2.pack(side=LEFT, padx=5)

        self.text3 = Entry(self.frame2, name="tekstowe 3")

        self.text3.config(state=DISABLED)
        self.text3.bind("<Return>", self.showContents)
        self.text3.pack(side=LEFT, padx=5)

        self.var = IntVar()
        for text, value in [('trojkowe', 3), ('osemkowe', 8), ('binarnie', 2)]:
            Radiobutton(self, text=text, value=value, variable=self.var).pack(anchor=W)

    def ternary(self, n):
        if n == 0:
            return '0'
        nums = []
        while n:
            n, r = divmod(n, 3)
            nums.append(str(r))
        return ''.join(reversed(nums))

    def showContents(self, events):
        '''wyswietl zawartosc pola'''
        # wyswietl nazwe pola tekstowego generujaca zdarzenia
        theName = events.widget.winfo_name()
        # podsaw zawartosc tego pola do zmiennej pomnizej


        theContents = events.widget.get()
        '''showinfo("komunikat", theName + ": " + int(self.var.get()))
        showinfo("komunikat", theName + ": " + oct(int(theContents)))

        showinfo("komunikat", theName + ": " + self.ternary(int(theContents)))'''

        if self.var.get()==8:
            self.text3.insert(INSERT, "osemkowo " + oct(int(theContents)))
            showinfo("komunikat", "osemkowo" + ": " + oct(int(theContents)))
        elif self.var.get() == 3:
            self.text3.insert(INSERT, "trojkow " + self.ternary(int(theContents)))
            showinfo("komunikat", "trojkow" + ": " + self.ternary(int(theContents)))
        elif self.var.get() == 2:
            self.text3.insert(INSERT, "binarnie " + bin(int(theContents)))
            showinfo("komunikat", "binarnie" + ": " + bin(int(theContents)))
        else :
            self.text3.insert(INSERT, "none " )
            showinfo("komunikat", "radiobutton!")


def main():
    EntryDemo().mainloop()


if __name__ == "__main__":
    main()