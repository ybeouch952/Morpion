from player import Player

class Box:
    def __init__(self):
        self.use = None
    
    def is_empty(self):
        return self.use is None
    
    def place(self,player):
        self.use = player
    
    def display(self):
        if self.use is None :
            return " "
        return self.use.symbol