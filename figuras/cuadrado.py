from figuras.figura import Figura

class Cuadrado(Figura):
    def __init__(self, nombre, lado):
        super().__init__(nombre)
        self.lado = lado

    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return 4 * self.lado