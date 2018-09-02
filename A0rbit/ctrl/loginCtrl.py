from mod.networking import Networking

class LoginCtrl:

    def __init__(self):
        self.networking = Networking.getInstance()
    
    def login(self):
        self.networking.login()
