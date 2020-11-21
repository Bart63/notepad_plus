from tkinter import *
from tkinter import filedialog
import pickle

noteList = []

root = Tk()
topFrame = Frame(root)
topFrame.pack()


def addNote():
	note = Note()
	noteList.append(note)


class Note:
	
	def __init__ (self):
		frame = Frame(root)
		frame.pack()

		self.noteButton = Label(frame, text = "Title")
		self.noteButton.pack(side = LEFT)

		self.delButton  = Button(frame, text = "delete", command = self.delMe)
		self.delButton.pack(side = LEFT)

		self.savebutton = Button(text = "save", command = self.save)
		self.savebutton.pack(side = LEFT)

		self.window = Tk()
		self.text = Text(self.window)
		self.text.pack()

	def __del__(self):
		print("Destructor called.")

	def delMe(self):
		self.noteButton.pack_forget()
		self.delButton.pack_forget()
		print("Bye.")
		del self

	def save(self):
		file = filedialog.asksaveasfile(defaultextension = ".txt",
										filetypes = [
											("text file",".txt"),
											("read only file", ".odt"),
											("PDF file", ".pdf"),
										])
		filetext = str(self.text.get(1.0,END))
		self.file.write(filetext)
		self.file.close()



addButton = Button(topFrame, text='Add', command = addNote)
addButton.pack()


root.mainloop()