from box import Box

class Grid:
    def __init__(self,size):
        self.size = size
        self.boxes = [[Box() for _ in range(size)] for _ in range(size)]

    def display(self,):
        for line in self.boxes:
            print(" | ".join(box.display() for box in line))
        print()
    
    def place(self,line,col,player):
        if self.boxes[line][col].is_empty():
            self.boxes[line][col].place(player)
            return True
        return False
    
    def is_full(self):
        for line in self.boxes :
            for box in line :
                if box.is_empty :
                    return False
        return True
