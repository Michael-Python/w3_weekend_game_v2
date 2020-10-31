import unittest 
from app.models.player import Player
from app.models.players import *

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("rock", "paper", "loss")
        
    def game_has_result(self):
        self.assertEqual("rock", self.player_1.selection_1)