import tkinter
import data

class Application(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root, width=420, height=320, borderwidth=4, relief='groove')
        self.root = root
        self.data = data.Data()
        self.pack()
        self.pack_propagate(0)
        self.init_widgets()

    def init_widgets(self):
        self.question = tkinter.Label(
            self, 
            font=('', 30),
            text=self.data.txt(), 
            width=20,
            height=3,
        )
        
        self.yes_btn = tkinter.Button(self, text='はい', command=lambda:self.next_content(True))
        self.no_btn = tkinter.Button(self, text='いいえ', command=lambda:self.next_content(False))

        self.question.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        self.yes_btn.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH)
        self.no_btn.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH)

    def next_content(self, isYes):
        if isYes:
            self.data.yes()
        else:
            self.data.no()

        self.question['text'] = self.data.txt()

        if not self.data.isQuestion():
            self.yes_btn.destroy()
            self.no_btn.destroy()
            self.question.pack(side=tkinter.TOP, expand=True, fill=tkinter.BOTH)


root = tkinter.Tk()
root.title('Gruppe Vier')
root.geometry('400x300')
app = Application(root=root)
app.mainloop()
