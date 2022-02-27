def check_win(player_num, current_player):
    pattern = [[0, 1, 2],[3, 4, 5],[6, 8, 7],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[6, 4, 2]]
    for x in pattern:
        if all(y in player_num[current_player] for y in x):
            return True  
        return False    
