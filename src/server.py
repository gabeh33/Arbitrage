from helpers import Tools
from draftkings import DK
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    nba_games = DK.get_nba_events()
    return nba_games

