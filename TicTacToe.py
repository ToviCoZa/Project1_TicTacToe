import random
    
p1_aligned_marks = 0
p2_aligned_marks = 0



player_1 = dict()
player_2 = dict()
player_1.update({'Name' : input("Player 1 please enter your name : ")})
player_2.update({'Name' : input("Player 1 please enter your name : ")})
player_1.update({'Symbol' : 'X'})
player_2.update({'Symbol' : 'O'})
player_1.update({'cellsPlayed' : [1, 2 , 3 , 4, 5, 6, 7, 8, 9]}) 
player_2.update({'cellsPlayed' : [1, 2 , 3 , 4, 5, 6, 7, 8, 9]}) 
player_1.update({'aligned_marks' : 0})
player_2.update({'aligned_marks' : 0})

board = {}

def whoIsGoingToStart():
    if random.randint(0,100) <= 50 : 
        starting_player = player_1
    else : 
        starting_player = player_2
    return(starting_player)

def create_board() :
    i = 1
    for i in range(10) :
        board.update({i: False})
    print(board)



def takeTurns(player):

    countOfTurns = 0
    hasGameEnded = False
    
    while countOfTurns < 9 and hasGameEnded == False:
        if countOfTurns % 2 == 0 :
            player = player_1
        else :
            player = player_2

        selected_cell = input("Please input the number of the cell you want to play in : ")
        if selected_cell.isdigit and len(selected_cell) == 1:
            for i in player.get('cellsPlayed') :
                if str(i) == selected_cell :
                    
                    player.get('cellsPlayed').remove(i)
                    print(player.get('cellsPlayed'))
                    cellToFill = board.get(selected_cell)
                    if cellToFill == False : board.update({str(selected_cell):player.get('Symbol')})
                    if checkWinCondition(player) == 'Win':
                        print("You win ! ")
                        hasGameEnded = True
                    countOfTurns += 1
                            
        else : pass
    print("It's a draw !")

def checkWinCondition(p):
    solutions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for i in solutions :
        for j in i :
            if board.get(j) == p.get('Symbol'):
                print(board.get(j))
                p.update('aligned_marks': player.get('aligned_marks'+ 1
                print(p.get(aligned_marks))
                if player.aligned_marks == 3 :
                    return 'win'


takeTurns(whoIsGoingToStart())