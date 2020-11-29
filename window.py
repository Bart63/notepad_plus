import os
from tkinter import *
import tkinter.filedialog

master = Tk()
master.geometry("200x200")

noteList = []

class Note:
	
    def __init__ (self):
        self.frame = Frame(master)
        self.frame.pack()

        self.noteButton = Label(self.frame, text = "Title")
        self.noteButton.pack(side= LEFT)


        self.delButton  = Button(self.frame, text = "delete", command=self.delMe)
        self.delButton.pack(side = LEFT)


    def __del__(self):
        print("Bye.")
        
    def delMe(self):
        if self in noteList: noteList.remove(self)
        self.frame.destroy()
        del self


def openNewWindow():
    newWindow = Toplevel(master)
    newWindow.title("Note Window")

    Label(newWindow, text = "Title of your note.").pack()
    Entry(newWindow).pack(fill="x")
    Label(newWindow, text = "Write your note here.").pack()
    Text(newWindow, height = 15, width = 55).pack(fill="both", expand=1)
    Label(newWindow, text = "Write your tags here.").pack()
    Entry(newWindow).pack(fill="x")
    attachments = Frame(newWindow)
    attachments.pack()
    Button(attachments, text="Add attachment", command = lambda: addAttachment(attachments)).pack(side=LEFT)
    Button(newWindow, text = "Save.", command = addNote).pack(side = "bottom")
	#save moze przekazac wartosc wiadomosci
	#i zapisac ja w obiekcie klasy button
	#command save'a wywoluje tworzenie obiektu note.


def addAttachment(frame):
    path = tkinter.filedialog.askopenfilename()
    Button(frame, text=path, command=lambda: openFile(path)).pack(side=LEFT)
    
def openFile(path):
    os.startfile(path, "open")
    

def addNote():
    note = Note()
    noteList.append(note) 

Label(master, text = "Main").pack()
Button(master, text = "New Note", command = openNewWindow).pack()
mainloop()