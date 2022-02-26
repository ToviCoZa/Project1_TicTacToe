import GridGenerator
import WinCondition


actualPlayer = True 
countOfTurns = 0
hasGameEnded = False


# while hasGameEnded == False :
#     print("game is on")


def gameLoop() :
    while countOfTurns < 9 :
        takeATurn()    
    print("It's a draw !")



def takeATurn() :
    # if actualPlayer == True :
    selected_cell = input("Please input the number of the cell you want to play in : ")
    selected_cell = int(selected_cell)
    cellToFill = GridGenerator.board.get(selected_cell)
    if cellToFill == False : GridGenerator.board.update({str(selected_cell):True})
    countOfTurns += 1
    actualPlayer = not actualPlayer
    if WinCondition.checkWinCondition() == 'Win':
        print("You win ! ")






