from player import Player

class Human(Player):
    def place(self,grid):
        size = grid.size
        while True:
            line = int(input(" Numéro de ligne : "))
            col = int(input(" Numéro de colonne : "))
            if  0 <= line < size and 0 <= col < size and grid.boxes[line][col].is_empty():
                return line, col
            print (" Case occupé ou hors grile, réessayez, ")
    