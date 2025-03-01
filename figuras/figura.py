from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def __str__(self):
        return f"{self.nombre}: Àrea = {self.area()}, Perímetro = {self.perimetro()}"