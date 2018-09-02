from ctrl.loginCtrl import LoginCtrl
from Tkinter import *

class Gui:
    
    def __init__(self):
        self.width = 208
        self.height = 128
        self.scale = 3

        self.master = Tk()
        self.master.title("A0rbit v1")

        self.canvas = Canvas(self.master, width=self.width*self.scale, height=self.height*self.scale)
        self.canvas.pack()

        # Canvas background
        self.canvas.create_rectangle(0, 0, self.width*self.scale, self.height*self.scale, fill="black")

        # Player info text
        self.playerInfoText = self.canvas.create_text(12, 12, anchor=NW, text="Loading..", fill="yellow")

        self.login()

        mainloop()
    
    def login(self):
        # Login to the game
        LoginCtrl().login()
