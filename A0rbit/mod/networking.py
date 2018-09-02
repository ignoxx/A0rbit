from clientInformation import *
from hero import Hero
import socket
import time
import threading


class Networking:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Networking.__instance == None:
            Networking()
        return Networking.__instance 

    def __init__(self):
        """ Virtually private constructor. """
        if Networking.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Networking.__instance = self
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(ADDR)

        # Hero object stored here
        self.hero = None 

    def login(self):
        self.send("LOGIN|{0}|{1}|{2}".format(UID, SID, CV))

        # now listen for incoming packets
        threading._start_new_thread(self.handlePackets, ())
    
    def logout(self):
        self.send("0|l")

        self.sock.close()

    def initHero(self, packet):

        playerData = {
            "name": packet[3],
            "userID": packet[2],
            "x": packet[12],
            "y": packet[13],
            "speed": packet[5],
            "credits": packet[24],
            "uridium": packet[25],
            "hp": packet[8],
            "hpmax": packet[9],
            "shd": packet[6],
            "shdmax": packet[7],
            "xp": packet[21],
            "honor": packet[22],
            "company": packet[15],
            "level": packet[23],
            "cloaked": packet[30]
        }

        print playerData

        if self.hero is None:
            self.hero = Hero(playerData)

    def handlePackets(self):
        while True:
            packet = self.sock.recv(16384)
            packet = packet.decode('utf-8')
            packet.replace("\r\r\r", "")
            
            nPacket = packet.split("\x00")
            
            for p in nPacket:
                if p != "":
                    packet = p.split("|")

                    if len(packet) >= 2:
                        if packet[0] == "ERR":
                            errCode = int(packet[1])

                            if errCode == 1:
                                print "Ship was destroyed"
                            elif errCode == 8:
                                print "Your Server ID or Current Map is wrong."
                            elif errCode == 41:
                                print "Invalid Session ID."
                            
                            break
                        
                        if packet[1] == "m": #new map
                            pass
                        elif packet[1] == "s": #create station
                            pass
                        elif packet[1] == "p": #create portal
                            pass
                        elif packet[1] == "I": #hero init
                            '''
                            args[2] == id;
                            args[3] == username;
                            args[4] == shipid;
                            args[5] == speed
                            args[6] == shield
                            args[7] == maxshield
                            args[8] == hp
                            args[9] == maxhp
                            args[10] == cargo
                            args[11] == maxcargo
                            args[12] == posx
                            args[13] == posy
                            args[14] == something to do with the last map
                            args[15] == faction/company
                            args[16] == clanid
                            args[17] == MaxLaserAmmo
                            args[18] == MaxRocketAmmo
                            args[19] == ExpansionTypeID
                            args[20] == Premium (true/false) in int
                            args[21] == experience points
                            args[22] == honor points
                            args[23] == level
                            args[24] == credits
                            args[25] == uridium
                            args[26] == jackpot (float)
                            args[27] == admin (21==admin)
                            args[28] == clan (string)
                            args[29] == galaxy gates done
                            args[30] == cloadked (int to bool)
                            '''
                            print "hero init"
                            self.initHero(packet)


                        elif packet[1] == "D": #hero update position
                            print "update hero position"
                            #self.updateHeroPosition(packet)
                        elif packet[1] == "C": #create ship
                            '''
                            args[2] == id
                            args[3] == shipid
                            args[4] == expansiontype id
                            args[5] == clan
                            args[6] == username
                            args[7] == posx
                            args[8] == posy
                            args[9] == faction/company (if company > 3; company = 0)
                            args[10] == clan id
                            args[11] == daily rank... do we need this??? i dont think so...
                            args[12] == set warn icon on map (bool)
                            args[13] == clan diplomacy (0 == neutral, 1 == allied, 2 == no attack pact, 3 == at war)
                            args[14] == galaxy gates done
                            args[15] == ???
                            args[16] == set npc (bool)
                            args[17] == cloaked (bool)
                            '''
                            pass
                        elif packet[1] == "R" or packet[1] == "K": #remove or destroy ship
                            pass
                        elif packet[1] == "c": #create box
                            pass#self.createBox(packet)
                        elif packet[1] == "2": #remove box
                            pass#self.removeBox(packet)
                        elif packet[1] == "LM":
                            pass#self.logMessages(packet)
                        elif packet[1] == "1": #ship movement
                            pass
                        elif packet[1] == "S": #set status
                            pass#print "set status (config?)"
    
    def send(self, data):
        data += "\r\n"
        
        self.sock.send(data.encode('utf-8'))