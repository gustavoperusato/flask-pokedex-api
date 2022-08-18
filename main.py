from flask import Flask, render_template
import requests
from models.pokemon import Pokemon
from flask.globals import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods = ['GET', 'POST'])
def buscar():
    pokemon = Pokemon(request.form["nome"].lower(),"")
    
    try:
        req = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon.nome}')
        reqtest = req.json()
        result = reqtest['sprites']['front_default']
        pokemon.foto = result

    except:
        return "Pokemon não encontrado"

    return render_template('index.html',
        nome = pokemon.nome,
        foto = pokemon.foto
    )

if __name__ == '__main__':
    app.run(debug=True)