from app.models.player import *

games = [
    { "selection_1" : "rock", "selection_2" : "paper", "result" : "lost to"},
    { "selection_1" : "rock", "selection_2" : "scissors", "result" : "won against"},
    { "selection_1" : "rock", "selection_2" : "rock", "result" : "tied with"},
    { "selection_1" : "paper", "selection_2" : "paper", "result" : "tied with"},
    { "selection_1" : "paper", "selection_2" : "scissors", "result" : "lost to"},
    { "selection_1" : "paper", "selection_2" : "rock", "result" : "won against"},
    { "selection_1" : "scissors", "selection_2" : "paper", "result" : "won against"},
    { "selection_1" : "scissors", "selection_2" : "scissors", "result" : "tied with"},
    { "selection_1" : "scissors", "selection_2" : "rock", "result" : "lost to"}
]

# tried a list, not successful
# player_1 = Player("rock", "paper", "lost to ")
# player_2 = Player("rock", "scissors", "won against ")
# player_3 = Player("rock", "rock", "tied with ")
# player_4 = Player("paper", "rock", "won against ")
# player_5 = Player("paper", "scissors", "lost to ")
# player_6 = Player("paper", "paper", "tied with ")
# player_7 = Player("scissors", "rock", "lost to ")
# player_8 = Player("scissors", "scissors", "tied with ")
# player_9 = Player("scissors", "paper", "won against ")

# players = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8, player_9]
