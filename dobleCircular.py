class NodoDC(object):
	"""docstring for NodoDC"""
	def __init__(self, nombre):
		
		self.nombre = nombre
		self.siguiente = None
		self.anterior  = None

class ListaDobleC(object):
	"""docstring for ListaDobleC"""
	def __init__(self):
		
		self.inicio = None
		self.final = None
		contador = 0
	
	def insertar(self, elemento):

		if self.inicio == None:
			self.inicio = elemento
			self.final = elemento
			self.inicio.siguiente= inicio
			self.inicio.anterior = final
			print ("se ingreso nodo a la lista")
			contador ++

		else:
			self.final.siguiente = elemento
			self.inicio.anterior = elemento
			self.elemento.anterior = final
			self.elemento.siguiente = inicio
			self.final = elemento
			print("la lista no estaba vacia")
			contador ++

	def recorrerLista(self):
		temporal = self.inicio
		contador1 =0

		while temporal != inicio:
			print(temporal.nombre)
			temporal = temporal.siguiente
			contador1 ++

	def function(self):
		pass
