from grid import Grid
from player import Player

class Game:
    def __init__(self,size,player1,player2):
        self.grid = Grid(size)
        self.players = [player1,player2]
        self.turn = 0
        self.size = size
        self.current_player = 0

    def play(self):
        while True:
            player = self.players[self.current_player]
            print("C'est au joueur " + str(player.index ))
            self.grid.display()

            line, col = player.place(self.grid)

            if self.grid.place(line, col,player):
                player.update_counters(line,col)
            
                if player.has_won(line,col):
                    self.grid.display()
                    print("Le" + str(player) + " a gagné ! ")
                    return True

                self.turn += 1

                if player.has_won(line,col) :
                    self.grid.display()
                    print("Le" + str(player) + " a gagné ! ")
                    return True
                
                if self.turn == self.size*self.size or self.grid.is_full() :
                    self.grid.display()
                    print ("Match Nul !")
                    return False
                    

                self.current_player = 1 - self.current_player
            else:
                print ("Case dèjà prise rejouer ")
        
