from mod.networking import Networking

class NetworkingCtrl:

    def __init__(self):
        self.networking = Networking.getInstance()
    
    def login(self, guiObj):
        self.networking.login(guiObj)
    
    def logout(self):
        self.networking.logout()
