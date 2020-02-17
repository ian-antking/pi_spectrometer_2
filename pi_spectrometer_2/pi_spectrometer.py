from tkinter import Tk

class App:
    def __init__(self, master):
        self.master = master
        self.master.title('Pi Spectrometer 2')

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()