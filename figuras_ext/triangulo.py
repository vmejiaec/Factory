from figuras.figura import Figura

class Triangulo(Figura):
    def __init__(self, nombre, base, altura):
        self.nombre = nombre
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2

    def perimetro(self):
        return 3 * self.base
    
    def __str__(self):
        return f'Triangulo: base={self.base}, altura={self.altura}'