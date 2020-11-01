from flask import render_template, request, redirect
from app import app
from app.models.game import games
from app.models.player import Player

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_result', methods=['GET', 'POST'])
def return_results():
    selection_1 = request.form['selection1']
    selection_2 = request.form['selection2']
    space = " "
    full_stop = ". "
    player_1 = request.form['username1']
    chose = " chose "
    player_2 = request.form['username2']

    # Investigate classes, again!!
    # player1 = Player(None)
#     player2 = Player(None)
#     Player.selection_1 = request.form['selection1']
    
#     player.name = request.form["name"]
#     Player.selection_2 = request.form['selection2']
#     space = " "
#     full_stop = ". "
#     player_1 = request.form['username1']
#     chose = " chose "
#     player_2 = request.form['username2']
#     comma = ", "

    for game in games:
        if  selection_1 == game["selection_1"] and selection_2 == game["selection_2"]:
            result = player_1 + chose + selection_1 + full_stop + player_2 + chose + selection_2 + full_stop + selection_1.title() +space+ game["result"] +space+ selection_2 + full_stop
        else:
            pass
    return result
    
    # return render_template('/', games = games[selection_1, result, selection_2])
