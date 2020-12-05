import os
from tkinter import *
import tkinter.filedialog
from pathlib import Path

master = Tk()
master.geometry("200x200")

noteList = []


class Note:

    def __init__(self, title, body, tags):
        self.title = title
        self.body = body
        self.tags = tags

        self.frame = Frame(master)
        self.frame.pack()

        self.noteButton = Label(self.frame, text=title)
        self.noteButton.pack(side=LEFT)

        self.delButton = Button(self.frame, text="delete", command=self.delMe)
        self.delButton.pack(side=LEFT)

    def __del__(self):
        print("Bye.")

    def delMe(self):
        if self in noteList: noteList.remove(self)
        self.frame.destroy()
        del self


def loadExisting():
    note_path = Path('./noteData.txt')
    if not note_path.stat().st_size == 0:
        with open('noteData.txt', 'r') as f:
            title = f.readline()
            body = f.readline()
            tags = f.readline()
            note = Note(title, body, tags)
            noteList.append(note)
            print(noteList)
        f.close()
    else:
        print('No notes to load')


def openNoteWindow():
    noteWindow = Toplevel(master)
    noteWindow.title("Note Window")

    Label(noteWindow, text="Title of your note.").pack()
    inputTitle = Entry(noteWindow)
    inputTitle.pack(fill="x")

    Label(noteWindow, text="Write your note here.").pack()
    inputBody = Text(noteWindow, height=15, width=55)
    inputBody.pack(fill="both", expand=1)

    Label(noteWindow, text="Write your tags here.").pack()
    inputTags = Entry(noteWindow)
    inputTags.pack(fill="x")

    attachments = Frame(noteWindow)
    attachments.pack()

    def addNote():
        title = inputTitle.get()
        body = inputBody.get("1.0", END)
        tags = inputTags.get()

        note = Note(title, body, tags)
        noteList.append(note)
        with open('noteData.txt', 'w') as f:
            f.write(note.title)
            f.write('\n')
            f.write(note.body)
            f.write(note.tags)

        print(noteList)
        print(note.body)
        print(note.tags)
        noteWindow.destroy()

    Button(attachments, text="Add attachment", command=lambda: addAttachment(attachments)).pack(side=LEFT)
    Button(noteWindow, text="Save.", command=addNote).pack(side="bottom")


def addAttachment(frame):
    path = tkinter.filedialog.askopenfilename()
    Button(frame, text=path, command=lambda: openFile(path)).pack(side=LEFT)


def openFile(path):
    os.startfile(path, "open")


Label(master, text="Main").pack()
Button(master, text="New Note", command=openNoteWindow).pack()
loadExisting()
mainloop()
