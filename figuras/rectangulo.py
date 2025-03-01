from figuras.figura import Figura

class Rectangulo(Figura):
	def __init__(self, nombre, base, altura):
		super.__init__(nombre)
		self.base = base
		self.altura = altura

	def area(self):
		return base * altura

	def perimetro(self):
		return 2*(base + altura)
