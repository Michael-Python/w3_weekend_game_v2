from flask import render_template, request, redirect
from app import app
from app.models.players import players
from app.models.player import Player

@app.route('/')
def index():
    return render_template('index.html', options=options)