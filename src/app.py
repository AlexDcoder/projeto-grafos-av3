"""
    Bibliotecas para entrar en cibtato com o front end
"""
from flask import Flask
import grafo

app = Flask(__name__)


@app.route("/")
def home_page():
    '''
        Página inicial do youtube
    '''
    return "Hello, World!"
