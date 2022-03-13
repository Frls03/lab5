from tkinter import *
from LED import *
class App:
    def __init__(self, window):
     self.screen=window
     self.title=StringVar()
     self.title.set('OFF')
     self.createLabel()
     self.createButton()

    def createLabel(self):
        self.label=Label(self.screen, textvariable=self.title).place(x=100, y=40)

    def createButton(self):
        self.btn=Button(self.screen, text='Enceder/apagar', command=lambda:self.LedOperation()).place(x=140, y=130)


    def LedOperation(self):
        if self.title.get()=='OFF':
            self.title.set('ON')
            onLed()
        else:
            self.title.set('OFF')
            offled()
            

root=Tk()
root.title('Aplicacion Arduino')
root.geometry("400x500")
appication=App(root)
root.mainloop()