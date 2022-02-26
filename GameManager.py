import GridGenerator
import WinCondition
import Player
import random

class GameManager:
    __instance = None
    actualPlayer = True 
    hasGameEnded = False
    countOfTurns = 0
    player_list = []
    # str1 = str()
    # str2 = str()

    # cellsPlayed = [1, 2 , 3 , 4, 5, 6, 7, 8, 9]

    def __init__(self):
        if GameManager.__instance is not None :
            raise Exception("Utiliser la méthode get_instance() pour obtenir une instance de l'objet")


    @staticmethod
    def get_instance() :
        if GameManager.__instance is None :
            print("Création du GameManager")
            GameManager.__instance = GameManager()
        return GameManager.__instance


    def initialization() :
        str1 = input("Player 1 please enter your name : ")
        str2 = input("Player 2 please enter your name : ")

        player_1 = Player.Player.__init__(Player, str1)
        player_2 = Player.Player.__init__(Player, str2)

        if random.randint(0,100) <= 50 : 
            starting_player = player_1
        else : 
            starting_player = player_2
        return(starting_player)

    def takeTurns(player) :
        player = player.get_instance()
        # if actualPlayer == True :
        while GameManager.countOfTurns < 9 and GameManager.hasGameEnded == False:
            selected_cell = input("Please input the number of the cell you want to play in : ")
            if selected_cell.isdigit and len(selected_cell) == 1:
                selected_cell = int(selected_cell)
                for i in player.self.cellsPlayed :
                    if i == selected_cell :
                        player.cellsPlayed.pop(i)
            
                        cellToFill = GridGenerator.board.get(selected_cell)
                        if cellToFill == False : GridGenerator.board.update({str(selected_cell):player.name})
                        GameManager.actualPlayer = not GameManager.actualPlayer
                        if WinCondition.checkWinCondition(player) == 'Win':
                            print("You win ! ")
                            GameManager.hasGameEnded = True
                        GameManager.countOfTurns += 1        
        print("It's a draw !")
        # GameManager.hasGameEnded == True







