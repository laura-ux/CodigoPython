#crear una funcion que solo imprima
def decirhola(nombre=''):
	print('hola {0}'.format(nombre))
decirhola('Ana')
decirhola()

#crear una funcion que te regrese un valor
def sumar(num1,num2):
	total= num1 + num2
	return total
sumar(2,3)
print(sumar(2,3),type(sumar(2,3)))
x=2
y=2
total= sumar(x,y)
print(total, type(total))
