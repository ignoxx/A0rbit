from mod.networking import Networking

class NetworkingCtrl:

    def __init__(self):
        self.networking = Networking.getInstance()
    
    def login(self):
        self.networking.login()
    
    def logout(self):
        self.networking.logout()
