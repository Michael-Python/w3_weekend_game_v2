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
    for game in games:
        if  selection_1 == game["selection_1"] and selection_2 == game["selection_2"]:
            result = game["result"]
            print(f"Player 1 {result} Player 2.")
        else:
            pass
    return result
    
    return render_template('/', games = games[selection_1, result, selection_2])
