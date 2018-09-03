import threading 
import time

class Ship:

    def __init__(self, shipData, gui):

        self.name = shipData["name"]
        self.shipID = shipData["shipID"]
        self.id = int(shipData["id"])
        self.x = int(shipData["x"])
        self.y = int(shipData["y"])
        self.company = int(shipData["company"])
        self.cloaked = int(shipData["cloaked"])
        self.isNpc = int(shipData["isNpc"])

        self.size = 2

        if self.id < 0:
            self.isNpc = True
            self.color = "red"
        else:
            self.isNpc = False
            self.color = "blue"

        self.gui = gui

        self.guiObj = self.gui.canvas.create_rectangle(
            (self.x/100 * self.gui.scale)-self.size, 
            (self.y/100 * self.gui.scale)-self.size, 
            (self.x/100 * self.gui.scale)+self.size, 
            (self.y/100 * self.gui.scale)+self.size, 
            fill=self.color
        )

        self.gui.ships.append(self)
        self.moving = False

    def lerp(self, a, b, t):
        return a + (b - a) * t
    
    def updatePosition(self, x, y, duration):
        pass

        # startTime = float(round(time.time() * 1000))
        # movingDuration = startTime + float(duration)

        # startX = float(self.x)
        # startY = float(self.y)

        # self.moving = True

        # while self.moving:
        #     time.sleep(.5)
        #     percent = (float(round(time.time() * 1000)) - startTime) / (movingDuration - startTime) 

        #     self.x = self.lerp(startX, int(x), percent)
        #     self.y = self.lerp(startY, int(y), percent)

        #     self.gui.canvas.delete(self.guiObj)

        #     self.guiObj = self.gui.canvas.create_rectangle(
        #         (self.x/100 * self.gui.scale)-self.size, 
        #         (self.y/100 * self.gui.scale)-self.size, 
        #         (self.x/100 * self.gui.scale)+self.size, 
        #         (self.y/100 * self.gui.scale)+self.size, 
        #         fill=self.color
        #     )

        #     if percent == 1.0:
        #         self.moving = False
        

    def hide(self):
        # self.gui.setColor(self.guiObj, "black")
        self.gui.canvas.delete(self.guiObj)
    
    def show(self):
        self.gui.setColor(self.guiObj, self.color)
    
    def remove(self):
        if self in self.gui.ships:
            self.gui.ships.remove(self)
        self.hide()