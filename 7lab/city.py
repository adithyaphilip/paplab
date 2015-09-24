class City:
    def __init__(self, name, *p):
        self.places = list(p)
        self.name = name
    def add(self, name):
        self.places.append(name)
    def remove(self, name):
        try: self.places.remove(name)
        except ValueError as e: print("How do you do away with that which was never done?")
    def disp(self):
        print(self.places)
c = City("Wasseypur")
c.disp()
c.add("Birmingham")
c.disp()
c.remove("LaluGhar")
c.disp()
d = City("Swaglation", "ChromeTown", "Epicafe")
d.disp()
d.add("Lalbagh")
d.disp()
d.remove("Lalbagh")
d.disp()
d.remove("hypocrisy")
