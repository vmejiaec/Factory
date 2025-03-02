import json
from figuras import FabricaFiguras
from figuras_ext.triangulo import Triangulo

# Leer datos desde JSON
def cargar_datos():
    try:
        with open('datos.json') as file:
            return json.load(file)
    except FileNotFoundError:
        print('No se encontro el archivo datos.json')
        return []
    except json.JSONDecodeError:
        print('Error al leer el archivo datos.json')
        return []

# main
if __name__ == "__main__":
    # Registrar la figura del triangulo
    FabricaFiguras.registrar_figura('Triangulo', Triangulo)
    
    datos = cargar_datos()
    figuras = FabricaFiguras.crear_figuras(datos)
    for figura in figuras:
        print(figura)
        print(f'Area: {figura.area()}')
        print(f'Perimetro: {figura.perimetro()}')
        print()