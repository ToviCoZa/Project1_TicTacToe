from typing_extensions import Self
import GridGenerator
import Player
import GameManager



GridGenerator.create_board()

GameManager.GameManager.get_instance()
first_player = GameManager.GameManager.initialization()
GameManager.GameManager.takeTurns(first_player)


