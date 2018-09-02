import time

class Hero:

    def __init__(self, playerData, networkingObj):

        self.name = playerData["name"]
        self.userID = playerData["userID"]
        self.x = float(playerData["x"])
        self.y = float(playerData["y"])
        self.speed = float(playerData["speed"])
        self.credits = int(playerData["credits"])
        self.uridium = int(playerData["uridium"])
        self.hp = int(playerData["hp"])
        self.hpmax = int(playerData["hpmax"])
        self.shd = int(playerData["shd"])
        self.shdmax = int(playerData["shdmax"])
        self.xp = int(playerData["xp"])
        self.honor = int(playerData["honor"])
        self.company = int(playerData["company"])
        self.level = int(playerData["level"])
        self.cloaked = int(playerData["cloaked"])

        self.networking = networkingObj

        self.size = 3
        self.color = "white"

        self.guiObj = self.networking.gui.canvas.create_rectangle(
            (self.x/100 * self.networking.gui.scale)-self.size, 
            (self.y/100 * self.networking.gui.scale)-self.size, 
            (self.x/100 * self.networking.gui.scale)+self.size, 
            (self.y/100 * self.networking.gui.scale)+self.size, 
            fill=self.color
        )

        self.networking.gui.setText(newText="{0} / {1} \n{2}/{3}\n{4}cr\n{5}uri".format(
            self.name, 
            self.userID, 
            self.hp, 
            self.shd,
            self.credits,
            self.uridium
        ))

        self.networking.send("1|5000|5000|{0}|{1}".format(
            self.x,
            self.y
        ))
    
    def hide(self):
        self.networking.gui.setColor(self.guiObj, "black")
    
    def show(self):
        self.networking.gui.setColor(self.guiObj, self.color)
    
    def updatePosition(self, x, y):
        self.networking.gui.canvas.delete(self.guiObj)

        self.x = float(x)
        self.y = float(y)
        self.guiObj = self.networking.gui.canvas.create_rectangle(
            (self.x/100 * self.networking.gui.scale)-self.size, 
            (self.y/100 * self.networking.gui.scale)-self.size, 
            (self.x/100 * self.networking.gui.scale)+self.size, 
            (self.y/100 * self.networking.gui.scale)+self.size, 
            fill=self.color
        )

        print "new position:", self.x, self.y
    
    def collectBoxes(self):
        return
        while True:
            pass

