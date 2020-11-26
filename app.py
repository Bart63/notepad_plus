from tkinter import *

class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, input_frame):
        """Destroys current frame and replaces it with a new one."""
        new_frame = input_frame(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack()

class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        Button(self, text = "Add note").pack()

        Label(self, text = "Switch to NotePage").pack()
        Button(self, text = "NotePage",
                  command = lambda: master.switch_frame(NotePage)).pack()


class NotePage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text = "Enter your note here:").pack()
        Text(self).pack()
        # you can get text from a text box using text_box.get("1.0", END)
        Label(self, text = "Switch to StartPage").pack()
        Button(self, text = "StartPage",
                  command = lambda: master.switch_frame(StartPage)).pack()


app = SampleApp()
app.mainloop()