from flask import render_template, request, redirect
from app import app
from app.models.players import players
from app.models.player import Player

@app.route('/')
def index():
    return render_template('index.html', players=players)

@app.route('/rock/scissors', methods=['POST'])
def return_results():
    selection_1 = request.form['selection1']
    selection_2 = request.form['selection2']
    return render_template('/')
