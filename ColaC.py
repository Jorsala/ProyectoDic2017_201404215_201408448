class NodoCola(object):
	"""docstring for NodoCola"""
	def __init__(self, nombreCan):
		
		self.nombreCan = nombreCan
		self.siguiente = None
		
class ColaCircular(object):
	"""docstring for ColaCircular"""
	def __init__(self):
		
		self.inicio = None
		self.final = None

	def insertar(self, elemento):
		if self.inicio == None:
			self.inicio = elemento
			self.elemento.siguiente = inicio
			self.final = inicio

		if self.inicio != None
			self.final.siguiente = elemento
			self.elemento.siguiente = inicio
			self.final = elemento

	def recorrerCola(self):
		self temporal = self.inicio
		if inicio != None:
			while temporal != None and temporal != inicio:
				self.temporal = temporal.siguiente
				print(temporal)

		else:
			print("la cola no tiene datos")


	def buscarNodo(self):

		self temporal = self.inicio
		encontrado = False

		if inicio != None:
			while temporal != None and temporal != inicio and encontrado != True:
				self.temporal = temporal.siguiente

				if !encontrado:
					print ("el nodo no se encontro")

				else:
					print("el nodo se encontro")

		else:
			print ("la Cola esta vacia")