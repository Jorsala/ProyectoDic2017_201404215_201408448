import commands


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
		self.total = 0




	def add(self, hijo):
		
		
		self.raiz = self.agg(hijo, self.raiz)



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


	def eliminar(self, idd):


		self.raiz = self.el(idd, self.raiz)

	def el(self, idd, nodo):

		if nodo == None:

			return None
		if nodo.nombre == idd:

			return self.juntar(nodo.izquierda, nodo.derecha)

		if nodo.nombre > idd:

			nodo.izquierda = self.el(idd, nodo.izquierda)

		else:

			nodo.derecha = self.el(idd, nodo.derecha)

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
		commands.getoutput('cp binario.png C:/Users/Jorge Salazar/Desktop')



	def ghojas(self, archi, raiz):
		if raiz != None:
			archi.write(str(raiz.nombre)+'[label="<f0>|<f1> Us:'+str(raiz.nombre)'|<f2>"]; \n')
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


	def buscar(self,raiz,idd):
		if raiz == None:

			return None
		elif raiz.nombre == idd:
			return raiz

		elif raiz.nombre > idd:
			return self.buscar(raiz.izquierda,idd)

		else:
			return self.buscar(raiz.derecha , idd)


	def modificar(self, idd, campo, nuevo):
		nodo = self.buscar(self.raiz , idd)

		if nodo != None:

			if campo == 'nombre':
				nodo.nombre = nuevo















"""prueba = arbol()
prueba.add(hoja('uno','dos','tres'))
prueba.add(hoja('z','dos','tres'))
prueba.add(hoja('dos','dos','tres'))
prueba.add(hoja('tres','dos','tres'))
prueba.add(hoja('cuatro','dos','tres'))
prueba.add(hoja('cinco','dos','tres'))
prueba.graficar()
prueba.modificar('z', 'line', 'zzozo' )
prueba.graficar()"""


		
		

