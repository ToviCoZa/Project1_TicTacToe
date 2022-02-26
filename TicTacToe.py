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
    if selected_cell.isdigit and len(selected_cell) == 1 and board[int(selected_cell)] == -1: #Si on est sur une case libre, on avance d'un tours
      board[int(selected_cell)] = countOfTurns;
      countOfTurns += 1
      if checkWinCondition() : break #Si quelqu'un à gagné
      if fullBoard() : #Si la grille est pleine
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
    if board[i[0]] != -1 and board[i[1]] != -1 and board[i[2]] != -1: #Si on test 3 cases remplies 
      if board[i[0]] % 2 == board[i[1]] % 2 == board[i[2]] % 2: #Si les 3 cases ont été placées par le meme joueur
        if i[0] % 2 == 0: #win du joueur 1
          print(player_1.get('Name') + " has won !")
        else: #win du joueur 2
          print(player_2.get('Name') + " has won !")
        return True
  return False


takeTurns()