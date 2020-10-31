from flask import render_template, request, redirect
from app import app
from app.models.players import games
from app.models.player import Player

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rock/scissors', methods=['GET', 'POST'])
def return_results():
    selection_1 = request.form['selection1']
    selection_2 = request.form['selection2']
    space = " "
    full_stop = ". "
    player_1 = "Player 1 chose "
    player_2 = ". Player 2 chose "
    comma = ", "

    for game in games:
        if  selection_1 == game["selection_1"] and selection_2 == game["selection_2"]:
            result = player_1 + selection_1 + player_2 + selection_2 + full_stop + selection_1.title() +space+ game["result"] +space+ selection_2 + full_stop
        else:
            pass
    return result
    
    # return render_template('/', games = games[selection_1, result, selection_2])
