from app.models.player import *

player_1 = Player("rock", "paper", "lost to ")
player_2 = Player("rock", "scissors", "won against ")
player_3 = Player("rock", "rock", "tied with ")
player_4 = Player("paper", "rock", "won against ")
player_5 = Player("paper", "scissors", "lost to ")
player_6 = Player("paper", "paper", "tied with ")
player_7 = Player("scissors", "rock", "lost to ")
player_8 = Player("scissors", "scissors", "tied with ")
player_9 = Player("scissors", "paper", "won against ")

players = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8, player_9]

print(player_1)