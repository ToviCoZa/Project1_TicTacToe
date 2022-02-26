import GridGenerator
import WinCondition

class GameManager:
    __instance = None
    actualPlayer = True 
    hasGameEnded = False
    countOfTurns = 0

    def __init__(self):
        if GameManager.__instance is not None :
            raise Exception("Utiliser la méthode get_instance() pour obtenir une instance de l'objet")


    @staticmethod
    def get_instance() :
        if GameManager.__instance is None :
            print("Création du GameManager")
            GameManager.__instance = GameManager()
        return GameManager.__instance



    def takeTurns() :
        # if actualPlayer == True :
        while GameManager.countOfTurns < 9 and GameManager.hasGameEnded == False:
            selected_cell = input("Please input the number of the cell you want to play in : ")
            if 
            selected_cell = int(selected_cell)
            cellToFill = GridGenerator.board.get(selected_cell)
            if cellToFill == False : GridGenerator.board.update({str(selected_cell):True})
            GameManager.countOfTurns += 1
            GameManager.actualPlayer = not GameManager.actualPlayer
            if WinCondition.checkWinCondition() == 'Win':
                print("You win ! ")
                GameManager.hasGameEnded = True
        print("It's a draw !")
        GameManager.hasGameEnded == True







