

class bird():
    def __init__(self, wings = 2, feet = 2, danger = 5):
        self.wings = wings
        self.feet = feet
        self.danger = danger
    def __repr__(self):
         pass
   

class owl(bird):
    def __init__(self,wings = 2,feet = 2,danger = 8):
        super().__init__(self,wings,feet,danger)
    def __repr__(self) -> str:
        return  (f"I am an owl, I have {self.wings} wings, {self.feet} feet and I am a {self.danger} on the danger scale, twoot twoot.")
    
    

class dodo(bird):
    def __init__(self,wings = 2,feet = 2,danger = 4):
        super().__init__(self,wings,feet,danger)
    def __repr__(self) -> str:
        rep = (f"I am a dodo, I have {self.wings} wings, {self.feet} feet and I am a {self.danger} on the danger scale, murgggh.")
        return rep