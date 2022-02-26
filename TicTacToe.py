import random

player_1 = ({'Name' : input("Player 1 please enter your name : ")})
player_2 = ({'Name' : input("Player 2 please enter your name : ")})

board = [-1] * 9

def whoIsGoingToStart():
  if random.randint(0,100) <= 50 : 
      starting_player = player_1
  else : 
      starting_player = player_2
  return(starting_player)

def draw_board() :
  for y in range(3):
    for x in range(3):
      if board[x + 3 * y] == -1: print(str(x + 3 * y) + "  ", end="")
      elif board[x + 3 * y] % 2 == 0: print("X  ", end="")
      else: print("O  ", end="")
    print()
  pass

def takeTurns():
  countOfTurns = 0
  if whoIsGoingToStart() is player_2:
    countOfTurns = 1 
  while True:
    draw_board()
    selected_cell = input("Please input the number of the cell you want to play in : ")
    if selected_cell.isdigit and len(selected_cell) == 1 and board[int(selected_cell)] == -1: 
      board[int(selected_cell)] = countOfTurns
      countOfTurns += 1
      if checkWinCondition() : break 
      if fullBoard() : 
        print("It's a draw !")
        break
  draw_board()
  

def fullBoard():
  for i in range(9):
    if board[i] == -1: return False
  return True


def checkWinCondition():
  solutions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  for i in solutions :
    if board[i[0]] != -1 and board[i[1]] != -1 and board[i[2]] != -1: #Testing 3 full cells 
      if board[i[0]] % 2 == board[i[1]] % 2 == board[i[2]] % 2: #Checking if unique player fulfilled the cells
        if i[0] % 2 == 0: 
          print(player_1.get('Name') + " has won !")
        else: 
          print(player_2.get('Name') + " has won !")
        return True
  return False


takeTurns()