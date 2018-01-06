import commands

class nodo(object):
	"""docstring for nodo"""
	def __init__(self, usuario, password):
		self.usuario =usuario
		self.password = password

		self.siguiente = None
		self.anterior = None

class ldoble(object):
	"""docstring for ldoble"""
	def __init__(self):
		self.primero = None

	def insertar(self, elemento):
		
		if self.primero == None:
			self.primero = elemento
		else:
			temporal = self.primero
			while temporal.siguiente != None:
				temporal = temporal.siguiente
			temporal.siguiente = elemento
			elemento.anterior = temporal

	def recorrer(self):
		
		temporal = self.primero
		while  temporal != None:
			print temporal.usuario
			temporal = temporal.siguiente

	def graficar1(self):
		archi = open('ldobleN.dot','w')
		archi.write('digraph Ilustrasion5{\n')
		archi.write('node [shape=record fontsize=10 fontname=\" Verdana\"style=filled];\n')
		contador = 0
		temporal = self.primero
		while temporal != None:
			contador = contador +1
			archi.write('node'+str(contador)+'[label="' + str(temporal.usuario)+ '"];\n')
			if temporal.siguiente != None:
				archi.write('node'+str(contador)+'->node'+str(contador+1)+'\n')
				archi.write('node'+str(contador+1)+'->node'+str(contador)+'\n')
			temporal = temporal.siguiente
		archi.write('\n}')
		archi.close()	
		commands.getoutput('dot -Tpng ldobleN.dot -o ldobleN.png')
		commands.getoutput('xdg-open ldobleN.png')


	def eliminar(self, indice):
		
		if self.primero != None:
			temporal = self.primero
			contador = 0
			while temporal != None:
				
		
				if contador == 0 and self.primero.siguiente != None and contador == indice:
					self.primero = self.primero.siguiente
					self.primero.anterior = None
					return '0'
				if contador == 0 and self.primero.siguiente == None and contador == indice:
					self.primero.siguiente = None
					self.primero.anterior = None
					self.primero = None
					return '0'
				
				elif contador == indice and temporal.siguiente == None:

					temporal.anterior.siguiente = None
					return '0'

				elif contador == indice:

					temporal.anterior.siguiente = temporal.siguiente

					temporal.siguiente.anterior = temporal.anterior
					return '0'

				contador = contador+1
				temporal = temporal.siguiente
		

prueba = ldoble()
for y in range(0,10):
	prueba.insertar(nodo(y,y))

prueba.recorrer()
print("\n")
prueba.eliminar(9)
prueba.eliminar(5)
prueba.recorrer()
prueba.graficar1()