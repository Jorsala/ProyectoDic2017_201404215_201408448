import commands


class usuario(object):
	"""docstring for usuario"""
	def __init__(self, dato):
		self.dato = dato
		self.siguente = None
		self.anterior = None
		
class lusuario(object):
	"""docstring for lusuario"""
	def __init__(self):
		self.primero = None
		self.anterior = None

	def insertar(self, elemento):
		
		if self.primero == None:
			self.primero = elemento
			elemento.siguente = elemento
			elemento.anterior = elemento
		else: 
			temporal = self.primero
			while temporal.siguente != self.primero:
				temporal = temporal.siguente

			self.primero.anterior= elemento
			temporal.siguente= elemento
			elemento.anterior = temporal
			elemento.siguente = self.primero

	def recorrer(self):
		reporte=''
		temporal = self.primero
		while temporal.siguente!= self.primero:
			reporte = str(reporte)+str(temporal.dato)+'->'
			temporal = temporal.siguente
		reporte =str(reporte)+str(temporal.dato)
		print 'Usuarios:'
		print reporte
		re = ''
		while temporal!= self.primero:
			re= str(re)+str(temporal.dato)+'->'
			temporal = temporal.anterior

		re = str(re)+str(temporal.dato)
		print re	
	


	def eliminar(self, dato):
		temporal = self.primero
		bandera = False
		if temporal!=None:

			if dato == self.primero.dato:


				self.primero = self.primero.siguente
				temporal.anterior.siguente = temporal.siguente
				temporal.siguente.anterior = temporal.anterior
				bandera = True


			while temporal.siguente!= self.primero and bandera == False:
				if temporal.dato == dato and bandera == False:
					
					temporal.anterior.siguente = temporal.siguente
					temporal.siguente.anterior = temporal.anterior
					bandera = True
					

				temporal = temporal.siguente

			if temporal.dato == dato and bandera == False:
				temporal.anterior.siguente = temporal.siguente
				temporal.siguente.anterior = temporal.anterior


	def graficar(self):
		archi = open('ldoble.dot','w')
		archi.write('digraph Ilustrasion5{\n')
		archi.write('node [shape=record fontsize=10 fontname=\" Verdana\"style=filled];\n')
		contador = 0
		aux =0
		temporal = self.primero

		if self.primero != None:
			while temporal.siguente != self.primero:
			
				archi.write('node'+str(contador)+'[label="' + str(temporal.dato)+'"];\n')
				if temporal.siguente != self.primero:
					archi.write('node'+str(contador)+'->node'+str(contador+1)+'\n')

				temporal = temporal.siguente
				contador = contador +1

			archi.write('node'+str(contador)+'[label="' + str(temporal.dato)+'"];\n')	
			archi.write('node'+str(0)+'->node'+str(contador)+'\n')
			aux = contador

			temporal=self.primero
			while temporal.siguente != self.primero:
			
				if temporal.siguente != self.primero:
					archi.write('node'+str(contador)+'->node'+str(contador-1)+'\n')

				temporal = temporal.siguente
				contador = contador-1

			
			archi.write('node'+str(aux)+'->node'+str(0)+'\n')



		archi.write('\n}')
		archi.close()	
		commands.getoutput('dot -Tpng ldoble.dot -o ldoble.png')
		commands.getoutput('xdg-open ldoble.png')
		commands.getoutput('cp ldoble.png ')


		
lista = lusuario()
lista.insertar(usuario('prueba1'))
lista.insertar(usuario('prueba2'))
lista.insertar(usuario('prueba3'))
lista.insertar(usuario('prueba4'))
lista.insertar(usuario('prueba5'))
lista.insertar(usuario('prueba6'))
lista.insertar(usuario('prueba7'))
lista.insertar(usuario('prueba8'))
lista.insertar(usuario('prueba9'))
lista.eliminar('prueba1')
lista.graficar()
lista.recorrer()

