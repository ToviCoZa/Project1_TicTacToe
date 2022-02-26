import GameManager

class Player() :
    __instance = None

    def __init__(self, name): 
        self.name = name
        print("i am " + self.name)
        GameManager.GameManager.get_instance().player_list.append(self.name)
        print(GameManager.GameManager.get_instance().player_list)
        self.aligned_marks = 0
        self.cellsPlayed = [1, 2 , 3 , 4, 5, 6, 7, 8, 9]

    @staticmethod
    def get_instance() :
        Player.__instance = Player()
        return Player.__instance
        

