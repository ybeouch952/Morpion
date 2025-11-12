from player import Player
import random

class Bot(Player):
    last_line = 0
    last_column = 0
    def place(self,grid):
        size = grid.size
        trynumber = 0
        while trynumber < 100:
            line = random.randint(0, size-1)
            col = random.randint(0, size-1)
            if grid.boxes[line][col].is_empty() : 
                return line, col
            trynumber += 1

        for line in range(self.last_line,size):
            self.last_line = line
            for col in range(0,size):
                if col == size -1:
                    self.last_column = 0
                    self.last_line += 1
                else:
                    self.last_column = col + 1
                if grid.boxes[line][col].is_empty() :
                    return line, col