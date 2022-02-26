import random
import Player



def initialization() :
    player_1 = input("Player 1 please enter your name : ")
    player_2 = input("Player 2 please enter your name : ")
    Player.__init__(player_1)
    Player.__init__(player_2)
    if random.randint(0,100) <= 50 : starting_player = player_1 
    else : starting_player = player_2
    return(starting_player)

