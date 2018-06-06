#!/usr/bin/python
#from live_test import---------------------------------- 
from Tkinter import Tk, Text, BOTH, W, N, E, S, END, Menu, Listbox
from ttk import Frame, Button, Label, Style
import os
import sys
import tkMessageBox
import tkFileDialog

class Nids_UI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Network Intrusion Detection System")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text="Data Log")
        lbl.grid(sticky=W, pady=4, padx=5)
		
        self.area = Text(self)
        sys.stdout = self
        self.area.grid(row=1, column=0, columnspan=2, rowspan=4,
            padx=5, sticky=E+W+S+N)

        abtn = Button(self, text=" Start Checking",command=self.OnButtonStart)
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text=" Stop Checking ",command=self.OnButtonStop)
        cbtn.grid(row=2, column=3, pady=4)

        hbtn = Button(self, text="View Log",command=self.OnLoad)
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text="Close",command=self.OnButtonClose)
        obtn.grid(row=5, column=3)
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.OnLoad)
        fileMenu.add_command(label="Exit", command=self.OnButtonClose)
        menubar.add_cascade(label="File", menu=fileMenu)
        self.parent.bind('<Control-c>',self.OnButtonClose)

    def OnLoad(self):
        ftypes = [('Python files', '*.txt')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.area.insert(END, text)

    def readFile(self, filename):
        f = open(filename, "r")
        text = f.read()
        return text

    def write(self, txt):
       self.area.insert(END,str(txt))

    def OnButtonStart(self):
    	#echo ubuntu | sudo -S COMMAND HERE
    	message = os.system("python live_test.py")
        #execfile("live_test.py")
        #CALL a function here
        if message == "Anamolous":
            tkMessageBox.showinfo( "Detector", "WARNING!!! Intrusion Detected!!")
        else :
            tkMessageBox.showinfo( "Detector", "No intrusion detected!!")

    def OnButtonStop(self):
        tkMessageBox.showinfo( "Detector", "Detection Stopped!!")

    def OnButtonClose(self):
        self.parent.destroy()


def main():
    root = Tk()
    root.geometry("350x300+300+300")
    app = Nids_UI(root)
    root.mainloop()


if __name__ == '__main__':
    main()

