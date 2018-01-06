import commands
import listadejuegos
class hoja(object):
	"""docstring for nodob"""
	def __init__(self, nombre):
		
		self.nombre = nombre

		self.derecha = None
		self.izquierda = None

class arbol(object):
	"""docstring for arbol"""
	def __init__(self):
	
		self.raiz = None
		self.contador = 0


	def add(self, hijo):
		
		
		self.raiz = self.agg(hijo, self.raiz)
		self.contador = self.contador + 1


	def agg(self, hijo, raiz):
		
		if raiz == None:
			raiz = hijo
			return raiz

		if raiz.nombre == hijo.nombre:
			pass
		elif raiz.nombre > hijo.nombre:
			raiz.izquierda = self.agg(hijo, raiz.izquierda)
		else:
			raiz.derecha = self.agg(hijo, raiz.derecha)

		return raiz

	
	def graficar(self):
		archi= open('binario.dot','w')
		archi.write('digraph arbol{ \n')
		archi.write('node[shape=record]\n')
		self.ghojas(archi, self.raiz)
		self.enlazes(archi, self.raiz)
		archi.write('} \n')
		archi.close()

		commands.getoutput('dot -Tpng binario.dot -o binario.png')
		commands.getoutput('xdg-open binario.png')

	def ghojas(self, archi, raiz):
		if raiz != None:
			archi.write(str(raiz.nombre)+'[label="<f0>|<f1> Cancion: '+str(raiz.nombre) + '|<f2>"]; \n')
			self.ghojas(archi, raiz.izquierda)
			self.ghojas(archi, raiz.derecha)


	def enlazes(self, archi, raiz):
		if raiz != None:
			if raiz.izquierda!= None:
				archi.write(str(raiz.nombre)+':f0->'+str(raiz.izquierda.nombre)+' \n')
			if raiz.derecha !=None:
				archi.write(str(raiz.nombre)+ ':f2->'+str(raiz.derecha.nombre)+ '\n')
			self.enlazes(archi, raiz.izquierda)
			self.enlazes(archi, raiz.derecha)
#----------------------------------------------------------------------------------------------

	def eliminar(self, nombre):


		self.raiz = self.el(nombre, self.raiz)
		#self.raiz = self.balance.equilibrar(self.raiz)

	def el(self, nombre, nodo):
		
		if nodo == None:

			return None
		if nodo.nombre == nombre:

			return self.juntar(nodo.izquierda, nodo.derecha)

		if nodo.nombre > nombre:

			nodo.izquierda = self.el(nombre, nodo.izquierda)

		else:

			nodo.derecha = self.el(nombre, nodo.derecha)

		return nodo

	def juntar(self, izq, der):
		
		if izq == None:
			return der

		if der== None:
			return izq

		mitad = self.juntar(izq.derecha, der.izquierda)
		izq.derecha = mitad
		der.izquierda = izq
		return der 

#------------------------------------------------------------------------------------------------

	def buscar(self,raiz,idd):
		if raiz == None:

			return None
		elif raiz.nombre == idd:
			return raiz

		elif raiz.nombre > idd:
			return self.buscar(raiz.izquierda,idd)

		else:
			return self.buscar(raiz.derecha , idd)





prueba1 = arbol()
prueba1.add(hoja('uno'))
prueba1.add(hoja('dos'))
prueba1.add(hoja('tres'))
prueba1.add(hoja('cuatro'))
prueba1.add(hoja('fierro'))
prueba1.add(hoja('canada'))
prueba1.add(hoja('hola'))
prueba1.add(hoja('comida'))
prueba1.add(hoja('zop'))
prueba1.eliminar('uno')
prueba1.graficar()
#print prueba.buscar(prueba.raiz, 'cinco').contra

		
		

