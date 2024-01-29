def frotar(n_frases: int = 1) -> list():
    with open('frase.txt', 'r') as f:
        frase = f.read()
    frases = [frase] * n_frases
    return frases