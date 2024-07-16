from Lexer import Lexer

class Jerarquia:
	def __init__(self, operacion:str):
		self.simbolos = ['*', '/', "+", '-']
		self.lx = Lexer()
		self.procedimientoAlmacenado = operacion.split(" ")
		self.productoActual = 0

	def organizarEjecucion(self):
		"""
		No tiene `parametros` resuelve la operacion segun las 
		jerarquia de las matematicas
		"""
		while True:
			if(self.procedimientoAlmacenado.__contains__("*")):
				self.contieneElemento("*")
				continue

			if self.procedimientoAlmacenado.__contains__("/"):
				self.contieneElemento("/")
				continue

			if self.procedimientoAlmacenado.__contains__("-"):
				self.contieneElemento("-")
				continue

			if self.procedimientoAlmacenado.__contains__("+"):
				self.contieneElemento("+")
				continue
			
			if (len(self.procedimientoAlmacenado) <= 2):
				return f"El resultado es: {self.productoActual}"
			
	def contieneElemento(self, elemento):
		index = self.procedimientoAlmacenado.index(elemento) #contiene el operador actual
		self.actualizarDatos(index) #actualiza los datos para obtener el producto

	def actualizarDatos(self, index:int):
		#obtencion de los datos
		previo = self.procedimientoAlmacenado[index - 1]
		actual = self.procedimientoAlmacenado[index]
		siguiente = self.procedimientoAlmacenado[index + 1]

		#ejecuto las operaciones basicas
		self.productoActual = self.lx.ejecucion(previo, actual, siguiente)
		del self.procedimientoAlmacenado[index - 1: index + 2] #elimino la parte que evalue
		self.procedimientoAlmacenado.insert(index - 1, self.productoActual) # inserto  la procedimientoAlmacenado resultante

jr = Jerarquia("2 * 7 / 2 + 3 - 4")
print(jr.organizarEjecucion())