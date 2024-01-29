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
    numero_frases = random.randint(0, 10)
    frases = frotar(numero_frases)
    return 'Hola, mundo! Aquí tienes {} frases: {}'.format(numero_frases, frases)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

