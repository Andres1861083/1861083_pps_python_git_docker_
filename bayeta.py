from mongo import inicializar, consultar, insertar_frase
import random

# Inicializar la colección
inicializar()
def frotar(n_frases: int = 1) -> list:
    if n_frases <= 0:
        raise ValueError('El número de frases debe ser mayor que 0')

    # Utilizar la función consultar de mongo.py para obtener frases desde MongoDB
    frases = consultar(n_frases)

    # Ajustar el tamaño de la muestra si es necesario
    n_frases = min(n_frases, len(frases))

    return random.sample(frases, n_frases)

def insertar_frase_bayeta(frase):
    insertar_frase(frase)