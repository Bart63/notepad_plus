import os
from tkinter import *
import tkinter.filedialog
from pathlib import Path

master = Tk()
master.geometry("200x200")

noteList = []

class Note:

    def __init__(self, title, body, tags, attachments):
        self.title = title
        self.body = body
        self.tags = tags
        self.attachments = attachments
        
        self.frame = Frame(master)
        self.frame.pack()

        self.noteButton = Label(self.frame, text=title)
        self.noteButton.pack(side=LEFT)

        self.delButton = Button(self.frame, text="delete", command=self.delMe)
        self.delButton.pack(side=LEFT)

    def delMe(self):
        if self in noteList: noteList.remove(self)
        self.frame.destroy()
        clear()
        for n in noteList:
            save(n.title, n.body, n.tags, n.attachments)
        del self

def loadExisting():
    note_path = Path('./noteData.txt')
    if not note_path.stat().st_size == 0:
        with open('noteData.txt', 'r') as f:
            while True:
                title = f.readline().rstrip()
                if title == '':
                    break
                body = f.readline().rstrip()
                tags = f.readline().rstrip()
                attachments = f.readline().rstrip()
                note = Note(title, body, tags, attachments)
                noteList.append(note)
        f.close()

def openNoteWindow():
    noteWindow = Toplevel(master)
    noteWindow.title("Note Window")

    def killWindow():
        noteWindow.destroy()

    Label(noteWindow, text="Title of your note.").pack()
    inputTitle = Entry(noteWindow)
    inputTitle.pack(fill="x")

    Label(noteWindow, text="Write your note here.").pack()
    inputBody = Entry(noteWindow)
    inputBody.pack(fill="both", expand=1)

    Label(noteWindow, text="Write your tags here.").pack()
    inputTags = Entry(noteWindow)
    inputTags.pack(fill="x")

    attachments = Frame(noteWindow)
    attachments.pack()
    
    Button(attachments, text="Add attachment", command=lambda: addAttachment(attachments)).pack(side=LEFT)
    Button(noteWindow, text="Save.", command=lambda: combine_funcs(
        addNote(inputTitle, inputBody, inputTags, attachments), killWindow())
        ).pack(side="bottom")

def addNote(inputTitle, inputBody, inputTags, inputAttachments):
    title = inputTitle.get()
    body = inputBody.get()
    tags = inputTags.get()
    
    attachmentsList = []
    attChildren = inputAttachments.winfo_children()
    
    attachments = ""
    
    for i in range(1, len(attChildren), 2):
        if i>2: attachments += ";"
        attachments += attChildren[i]['text']

    note = Note(title, body, tags, attachments)
    save(note.title, note.body, note.tags, note.attachments)
    noteList.append(note)

def clear():
    open('noteData.txt', 'w').close()

def save(title, body, tags, attachments):
    with open('noteData.txt', 'r+') as f:
        f.readlines()

        if len(title): f.write(title + '\n')
        else: f.write('\n')

        if len(body): f.write(body + '\n')
        else: f.write('\n')

        if len(tags): f.write(tags + '\n')
        else: f.write('\n')

        if len(attachments): f.write(attachments + '\n')
        else: f.write('\n')
        

def addAttachment(frame):
    path = tkinter.filedialog.askopenfilename()
    att = Button(frame, text=path, command=lambda: openFile(path))
    att.pack(side=LEFT)
    xButton = Button(frame, text="X", command=lambda: delAttachment(att, xButton))
    xButton.pack(side=LEFT)

def delAttachment(attachment, xButton):
    attachment.destroy()
    xButton.destroy()

def openFile(path):
    os.startfile(path, "open")

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

Label(master, text="Main").pack()
Button(master, text="New Note", command=openNoteWindow).pack()
loadExisting()
mainloop()
