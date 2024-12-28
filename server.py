import sys
import os

# Add the 'src' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from helpers import Tools
from draftkings import DK
from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    nba_games = DK.get_nba_events()
    return nba_games

if (__name__ == "__main__"):
    app.run()