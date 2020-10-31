from app.models.player import *

games = [
    { "game_id" : 1, "selection_1" : "rock", "selection_2" : "paper", "result" : "lost to"},
    { "game_id" : 2, "selection_1" : "rock", "selection_2" : "scissors", "result" : "won against"},
    { "game_id" : 3, "selection_1" : "rock", "selection_2" : "rock", "result" : "tied with"},
    { "game_id" : 4, "selection_1" : "paper", "selection_2" : "paper", "result" : "tied with"},
    { "game_id" : 5, "selection_1" : "paper", "selection_2" : "scissors", "result" : "lost to"},
    { "game_id" : 6, "selection_1" : "paper", "selection_2" : "rock", "result" : "won against"},
    { "game_id" : 7, "selection_1" : "scissors", "selection_2" : "paper", "result" : "won against"},
    { "game_id" : 8, "selection_1" : "scissors", "selection_2" : "scissors", "result" : "tied with"},
    { "game_id" : 9, "selection_1" : "scissors", "selection_2" : "rock", "result" : "lost to"}
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

# def input_results(games):
#     input_1="paper"
#     input_2="scissors"
#     for game in games:
#         if  input_1 == game["selection_1"] and input_2 == game["selection_2"]:
#             result = game["result"]
#             print(f"Player 1 {result} Player 2.")
#         else:
#             pass
#     return(games)
        
# input_results(games)