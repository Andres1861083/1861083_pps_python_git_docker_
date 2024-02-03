from pymongo import MongoClient

def instanciar():
    # Conexión con el motor de Mongo
    cliente_mongo = MongoClient('mongodb://mongodb:27017')
    
    # Conexión con la BD (la crea si no existe)
    bd = cliente_mongo['bayeta']
    
    # Conexión con la colección
    frases_auspiciosas = bd['frases_auspiciosas']
    
    return frases_auspiciosas

def inicializar(ruta_archivo='frase.txt'):
    # Obtener la instancia de la colección
    frases_auspiciosas = instanciar()

    # Comprobamos que no se haya inicializado previamente
    if frases_auspiciosas.count_documents({}) == 0:
        # Leer datos desde el archivo
        with open(ruta_archivo, 'r') as f:
            datos = [{"frase": linea.strip()} for linea in f]

        # Inserción de datos
        frases_auspiciosas.insert_many(datos)

def consultar(n_frases):
    # Obtener la instancia de la colección
    frases_auspiciosas = instanciar()

    # Obtener frases aleatorias
    frases_aleatorias = list(frases_auspiciosas.aggregate([{'$sample': {'size': n_frases}}]))

    return [frase['frase'] for frase in frases_aleatorias]

    
