from figuras.figura import Figura
from math import pi

class Circulo(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio
    
    def area(self):
        return pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * pi * self.radio