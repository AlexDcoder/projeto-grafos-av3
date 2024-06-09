"""
    Bibliotecas para entrar en cibtato com o front end
"""
from flask import Flask
from pprint import pprint
app = Flask(__name__)

with open("videos.json", encoding="utf-8") as db:
    pprint(list(db))


@app.route("/home")
def home_page():
    '''
        Página inicial do youtube
    '''
    return "Hello, World!"
