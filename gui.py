from tkinter import *

noteList = []

root = Tk()
topFrame = Frame(root)
topFrame.pack()


def addNote():
	note = Note()
	noteList.append(note)

def switchPage():


class tkNote:
	
	def __init__ (self):
		frame = Frame(root)
		frame.pack()

		self.noteButton = Label(frame, text = "Title")
		self.noteButton.pack(side= LEFT)


		self.delButton  = Button(frame, text = "delete", command=self.delMe)
		self.delButton.pack(side = LEFT)


	def __del__(self):
		print("Bye.")

	def delMe(self):
		self.noteButton.pack_forget()
		self.delButton.pack_forget()
		del self


addButton = Button(topFrame, text='Add', command = addNote)
addButton.pack()

switchButton = Button(text = 'Switch', command = switchPage)
switchButton.pack()

root.mainloop()