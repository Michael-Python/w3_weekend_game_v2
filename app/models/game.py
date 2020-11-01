class Game:

    def __init__(self, selection_1, selection_2, result):
        self.selection_1 = selection_1
        self.selection_2 = selection_2
        self.result = result

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
# print(selection_1[3])