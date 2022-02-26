import imp
import GridGenerator

solutions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]


def checkWinCondition() :
    for i in solutions :
        aligned_marks = 0
        for j in i :
            if GridGenerator.board.get(j) :
                aligned_marks += 1
                if aligned_marks == 3 :
                    return 'win'
                
    


