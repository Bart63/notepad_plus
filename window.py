import os
import tkinter.filedialog
from pathlib import Path
from tkinter import *

import search as search

master = Tk()
master.geometry("300x400")
notes = Frame(master)
searchedNotes = Frame(master)
noteList = []


class Note:

    def __init__(self, title, body, tags, attachments):
        self.title = title
        self.body = body
        self.tags = tags
        self.attachments = attachments

        self.frame = Frame(notes)
        self.frame.pack()

        self.noteButton = Label(self.frame, text=title)
        self.noteButton.pack(side=LEFT)

        self.delButton = Button(self.frame, text="delete", command=self.delMe)
        self.delButton.pack(side=LEFT)

        self.openButton = Button(self.frame, text="open", command=self.openMe)
        self.openButton.pack(side=LEFT)

    def delMe(self):
        if self in noteList: noteList.remove(self)
        self.frame.destroy()
        clear()
        for n in noteList:
            save(n.title, n.body, n.tags, n.attachments)
        del self

    def getAttachementList(self):
        listAtt = self.attachments.split(';')
        return listAtt

    def openMe(self):
        title = self.title
        body = self.body
        tags = self.tags
        attachments = self.attachments
        noteWindow = Toplevel(master)
        noteWindow.title("Note Window")
        Label(noteWindow, text="Title of your note.").pack()
        inputTitle = Entry(noteWindow)
        inputTitle.insert(0, title)
        inputTitle.pack(fill="x")

        Label(noteWindow, text="Write your note here.").pack()
        inputBody = Entry(noteWindow) 
        inputBody.insert(0, body)
        inputBody.pack(fill="both", expand=1)

        Label(noteWindow, text="Write your tags here.").pack()
        inputTags = Entry(noteWindow)
        inputTags.insert(0, tags)
        inputTags.pack(fill="x")

        def killWindow():
            noteWindow.destroy()

        attList = self.getAttachementList()
        attachments = Frame(noteWindow)
        attachments.pack()
        Button(attachments, text="Add attachment", command=lambda: addAttachment(attachments)).pack(side=LEFT)
        for att in attList:
            if len(att)>1:
                addExistingAtt(attachments, att)
        Button(noteWindow, text="Save.", command=lambda: combine_funcs(
        addNote(inputTitle, inputBody, inputTags, attachments), killWindow(), self.delMe())
           ).pack(side="bottom")


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

    attChildren = inputAttachments.winfo_children()

    attachments = ""

    for i in range(1, len(attChildren), 2):
        if i > 2: attachments += ";"
        attachments += attChildren[i]['text']

    note = Note(title, body, tags, attachments)
    save(note.title, note.body, note.tags, note.attachments)
    noteList.append(note)


def clear():
    open('noteData.txt', 'w').close()


def save(title, body, tags, attachments):
    with open('noteData.txt', 'r+') as f:
        f.readlines()

        if len(title):
            f.write(title + '\n')
        else:
            f.write('\n')

        if len(body):
            f.write(body + '\n')
        else:
            f.write('\n')

        if len(tags):
            f.write(tags + '\n')
        else:
            f.write('\n')

        if len(attachments):
            f.write(attachments + '\n')
        else:
            f.write('\n')


def addAttachment(frame):
    path = tkinter.filedialog.askopenfilename()
    att = Button(frame, text=path, command=lambda: openFile(path))
    att.pack(side=LEFT)
    xButton = Button(frame, text="X", command=lambda: delAttachment(att, xButton))
    xButton.pack(side=LEFT)

def addExistingAtt(frame, path):
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


def searchNotes(text, maxNotes):
    clearSearchFrame()
    if text.strip():
        proceedSearch(text, maxNotes)
        searchedNotes.pack()
        notes.pack_forget()
    else:
        searchedNotes.pack_forget()
        notes.pack()


def getTitleList():
    listT = []
    for note in noteList:
        listT.append(note.title)
    return listT


def getTagsList():
    listT = []
    for note in noteList:
        listT.append(note.tags)
    return listT


def proceedSearch(inputText, maxNotes):
    searcher = search.Searcher()
    searchRes = searcher.Search(inputText, getTitleList(), getTagsList())

    maxIndex = maxNotes if len(searchRes) > maxNotes else len(searchRes)

    indexes = []
    for i in range(0, maxIndex):
        indexes.append(searchRes[i][0])
    fillSearchFrame(indexes)


def fillSearchFrame(indexes):
    for ind in indexes:
        note = Frame(searchedNotes)
        note.pack()
        noteButton = Label(note, text=noteList[ind].title)
        noteButton.pack(side=LEFT)

        delButt(ind, note)
        openButt(ind, note)

def delButt(ind, note):
    Button(note, text="delete", command=lambda: combine_funcs(noteList[ind].delMe()
                                                              , searchNotes("", 0))
           ).pack(side=LEFT)

def openButt(ind, note):
    Button(note, text="open", command=lambda: noteList[ind].openMe()).pack(side=LEFT)

def clearSearchFrame():
    for child in searchedNotes.winfo_children():
        child.destroy()


Label(master, text="Notepad#").pack()
nav = Frame(master)
Button(nav, text="New Note", command=openNoteWindow).pack()
searchText = Entry(nav)
searchText.pack(side=LEFT)
Button(nav, text="Search", command=lambda: searchNotes(searchText.get(), 3)).pack(side=LEFT)
Button(nav, text="X", command=lambda: searchNotes("", 0)).pack(side=LEFT)
nav.pack()
notes.pack()

loadExisting()
mainloop()
