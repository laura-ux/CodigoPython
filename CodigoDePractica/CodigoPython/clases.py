#crear una clase
class usuario:
	#constructor 
	def __init__(self, nombre, email, edad):
	    self.nombre = nombre
 	    self.email = email
	    self.edad = edad
	
	def saludos (self,num1=1):
	    print(num1)
	    return 'Me llamo {0} y tengo {1}'.format(self.nombre, self.edad)
	def tengo_cumple(self):
	    self.edad+=1
Ana= usuario('Ana Laura','ana@gmail.com',22)
print(type(Ana))
print(Ana.nombre)
print(Ana.saludos())

#extender la clase usuario
class cliente(usuario):
	def __init__(self, nombre,email,edad):
	    self.nombre = nombre
	    self.email = email
	    self.edad = edad
	    self.saldo = 0

	def establecer_saldo(self,saldo):
	    self.saldo=saldo

	def saludos(self):
	    return 'Me llamo {0}, tengo {1} y mi saldo es {2}'.format(self.nombre, self.edad, self.saldo)
Rufina_usuario = usuario ('Rufuna Madrid', 'rufina@yahoo.com', 2)
Rufina_cliente = cliente('Rufina Madrid','rufina@yahoo.com',2)
Rufina_cliente.establecer_saldo(5e10)
print(Rufina_cliente.saludos())
print(Rufina_usuario.saludos())
