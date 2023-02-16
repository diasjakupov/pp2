import json


class Entry:
    def __init__(self, dn, desc, speed, mtu):
        self.dn = dn
        self.desc = desc
        self.speed = speed
        self.mtu = mtu


class JsonParser:
    def __init__(self, file):
        self.raw = json.load(file)
        self.entries = []

    def __getAllDnValues(self):
        for i in self.raw["imdata"]:
            attributes = i["l1PhysIf"]["attributes"]
            self.entries.append(
                Entry(dn=attributes["dn"], desc=attributes["descr"], speed=attributes["speed"], mtu=attributes["mtu"]))

    def logData(self):
        self.__getAllDnValues()
        print("Interface Status")
        print("================================================================================")
        print("DN                                                 Description           Speed    MTU  ")
        print("-------------------------------------------------- --------------------  ------  ------")
        for i in self.entries:
            print(f"{i.dn:<50} {i.desc:<20}  {i.speed:<6}  {i.mtu:<6}")


with open("sample-data.json") as file:
    parser = JsonParser(file)
    parser.logData()
