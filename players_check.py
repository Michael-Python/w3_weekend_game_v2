
player_1 = ["rock", "paper", "lost to "]
player_2 = ["rock", "scissors", "won against "]
player_3 = ["rock", "rock", "tied with "]
player_4 = ["paper", "rock", "won against "]
player_5 = ["paper", "scissors", "lost to "]
player_6 = ["paper", "paper", "tied with "]
player_7 = ["scissors", "rock", "lost to "]
player_8 = ["scissors", "scissors", "tied with "]
player_9 = ["scissors", "paper", "won against "]

players = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8, player_9]

def input_results(self, players):
    selection_1 = ""
    selection_2 = ""
    input(selection_1)
    input(selection_2)
    for self.player in players:
        if player[0] == selection_1 and player[1] == selection_2:
            print(f"Player 1 chose {player[0]}. Player 2 chose {player[1]}. Player 1` {player[2]} Player 2.")
    return players

print(input_results(players))