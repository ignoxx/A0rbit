from ctrl.networkingCtrl import NetworkingCtrl
from Tkinter import *

class Gui:
    
    def __init__(self):
        self.width = 208
        self.height = 128
        self.scale = 3

        self.master = Tk()
        self.master.title("A0rbit v1")

        # what happens after closing the window?
        self.master.protocol("WM_DELETE_WINDOW", self.onClose)

        self.canvas = Canvas(self.master, width=self.width*self.scale, height=self.height*self.scale)
        self.canvas.pack()

        # Canvas background
        self.canvas.create_rectangle(0, 0, self.width*self.scale, self.height*self.scale, fill="black")

        # Player info text
        self.playerInfoText = self.canvas.create_text(12, 12, anchor=NW, text="Loading..", fill="yellow")

        # Store all bonusBoxes here
        self.bonusBoxes = list()

        self.login()

        mainloop()
    
    def setText(self, elementId = None, newText=""): 
        if elementId is None: elementId = self.playerInfoText
        self.canvas.itemconfig(elementId, text=newText)

    def setColor(self, elementId, newColor): 
        self.canvas.itemconfig(elementId, fill=newColor)
    
    def login(self):
        # Login to the game
        NetworkingCtrl().login(self)
    
    def onClose(self):
        NetworkingCtrl().logout()
        exit()
        
