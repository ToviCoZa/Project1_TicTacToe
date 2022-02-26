import GridGenerator

solutions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]


def checkWinCondition(player) :
    player = player.get_instance()
    for i in solutions :
        for j in i :
            if GridGenerator.board.get(j) == player.__name__ :
                print(GridGenerator.board.get(j))
                player.aligned_marks += 1
                print(player.aligned_marks)
                if player.aligned_marks == 3 :
                    return 'win'
                
    


