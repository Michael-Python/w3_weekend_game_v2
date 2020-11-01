import unittest 
from app.models.player import Player
from app.models.players import *
from app.models.game import *

class TestPlayer(unittest.TestCase):
    def test_player_1_has_choice(self, games):
        self.assertEqual("rock", games.get_game_results(games[0]))
