# app.py
import random
from bayeta import frotar
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/frotar/<int:n_frases>')
def obtener_frases(n_frases):
    frases = frotar(n_frases)
    frases_dict = []
    for frase in frases:
        frases_dict.append({'frase': frase})
    return jsonify(frases_dict)

@app.route('/')
def hola_mundo():
    return "Hola Mundo!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)