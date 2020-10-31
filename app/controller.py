from flask import render_template, request, redirect
from app import app
from app.models.options import *
from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html', options=options)