from graphviz import render
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
class nodo(object):
	"""docstring for nodo"""
	def __init__(self, dato):
		self.dato =dato
		self.siguiente = None
		self.anterior = None

class ljuegos(object):
	"""docstring for ljuegos"""
	def __init__(self):
		self.primero = None

	def insertar(self, elemento):
		
		if self.primero == None:
			self.primero = elemento
			self.primero.siguiente = None
			self.primero.anterior = None
		else:
			temporal = self.primero
			while temporal.siguiente != None:
				temporal = temporal.siguiente
			temporal.siguiente = elemento
			elemento.anterior = temporal

	def recorrer(self):
		
		temporal = self.primero
		while  temporal != None:
			print (temporal.oponente)
			temporal = temporal.siguiente

	def eliminar(self, indice): #la eliminacion es por indice
		
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
		




	def modificar(self):
		pass

	def graficar(self):
		archi = open('cola.dot','w')
		archi.write('digraph Ilustrasion5{\n')
		archi.write('node [shape=record fontsize=10 fontname=\" Verdana\"style=filled];\n')
		contador = 0
		temporal = self.primero
		while temporal != None:
			contador = contador +1
			archi.write('node'+str(contador)+'[label="' + str(temporal.dato)+'"];\n')
			if temporal.siguiente != None:
				archi.write('node'+str(contador)+'->node'+str(contador+1)+'\n')
				
			temporal = temporal.siguiente
		archi.write('\n}')
		archi.close()	
		"""commands.getoutput('dot -Tpng cola.dot -o cola.png')
		commands.getoutput('xdg-open cola.png')
		commands.getoutput('cp cola.png ')"""
		render('dot', 'png', 'cola.dot') 

prueba = ljuegos()
for y in range(0,7):
	prueba.insertar(nodo(str(y)))


prueba.eliminar(5)


prueba.graficar()