import random

frases = []
with open('frase.txt', 'r') as f:
    for frase in f:
        frases.append(frase)

def frotar(n_frases: int = 1) -> list():
    if n_frases <= 0:
        raise ValueError('El número de frases debe ser mayor que 0')

    return random.sample(frases, n_frases)
