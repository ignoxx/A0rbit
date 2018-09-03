from settings import *

class BonusBox:

    def __init__(self, data, gui):
        
        self.boxID = int(data["boxID"])
        self.x = int(data["x"])
        self.y = int(data["y"])
        self.type = int(data["type"])
        self.size = 2

        self.gui = gui

        if self.type == 1:
            self.color = "orange"
        else:
            self.color = "yellow"
            self.gui.bonusBoxes.append(self)
        
        

        self.guiObj = self.gui.canvas.create_rectangle(
            (self.x/100 * self.gui.scale)-self.size, 
            (self.y/100 * self.gui.scale)-self.size, 
            (self.x/100 * self.gui.scale)+self.size, 
            (self.y/100 * self.gui.scale)+self.size, 
            fill=self.color
        )

        

    def hide(self):
        # self.gui.setColor(self.guiObj, "black")
        self.gui.canvas.delete(self.guiObj)
    
    def show(self):
        self.gui.setColor(self.guiObj, self.color)
    
    def remove(self):
        if self in self.gui.bonusBoxes:
            self.gui.bonusBoxes.remove(self)
        self.hide()
    
