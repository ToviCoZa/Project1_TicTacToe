import random
player_1 = input("Player 1 please enter your name : ")
player_2 = input("Player 2 please enter your name : ")

def initialization() :
    if random.randint(0,100) <= 50 : starting_player = player_1 
    else: starting_player = player_2
    print(starting_player)

initialization()