import json
from figuras.cuadrado import Cuadrado
from figuras.rectangulo import Rectangulo
from figuras.circulo import Circulo

# Mapeo de tipos a clases
TIPOS_FIGURAS = {
    'Cuadrado': Cuadrado,
    'Rectangulo': Rectangulo,
    'Circulo': Circulo
}

# Leer datos desde JSON
def cargar_datos():
    with open('datos.json') as file:
        return json.load(file)
    
# Crear lista de figuras
def crear_figuras(datos):
    figuras = []
    for dato in datos:
        tipo = dato.pop('tipo')
        clase = TIPOS_FIGURAS[tipo]
        if clase:
            figuras.append(clase(**dato))
    return figuras

# main
if __name__ == "__main__":
    datos = cargar_datos()
    figuras = crear_figuras(datos)
    for figura in figuras:
        print(figura)
        print(f'Area: {figura.area()}')
        print(f'Perimetro: {figura.perimetro()}')
        print()