# app.py
import random
from bayeta import frotar, insertar_frase_bayeta
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/frotar/<int:n_frases>')
def obtener_frases(n_frases):
    frases = frotar(n_frases)
    frases_dict = []
    for frase in frases:
        frases_dict.append({'frase': frase})
    return jsonify(frases_dict)

@app.route('/frotar/add', methods=['POST'])
def agregar_frases():
    try:
        data = request.get_json()
        nuevas_frases = data.get('frases', [])
        for frase in nuevas_frases:
            insertar_frase_bayeta(frase)
        return jsonify({"message": "Frases agregadas exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def hola_mundo():
    return "Hola Mundo!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)