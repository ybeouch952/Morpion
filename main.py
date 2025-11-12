from game import Game
from human import Human
from bot import Bot

def create_player(index):
    symbol = input("Symbole du joueur " + str(index) +" ")
    while True :
        is_bot = input("Le joueur est il un bot ? Si oui entrez O sinon entrez N !  ")
        if is_bot == "O" or is_bot == "o" :
            return Bot(symbol,index,size)
        elif is_bot == "N" or is_bot == "n" :
            return Human(symbol,index,size)
        else :
            print (" Veuillez recommencez et bien entrer O ou N ! ")


if __name__ =="__main__":
    compt = 0
    win = False
    size = int(input("Avec quelle taille de grille voulez vous jouer ?"))
    while win == False :
        size = size
        joueur1 = create_player(0)
        joueur2 = create_player(1)
        game = Game(size, joueur1, joueur2)
        win = game.play()
        compt += 1
    print ("Le compteur" + str(compt))
