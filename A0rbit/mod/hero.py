class Hero:

    def __init__(self, playerData):

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
