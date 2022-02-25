import random
player_1 = input("Please insert the player name: " )
player_2 = input("plese insert an another player name: " )

def initialization () :
    if random.randint(0,100) <=50: 
        starting_player = player_1 
    else:
        starting_player = player_2
    print(starting_player)

initialization()