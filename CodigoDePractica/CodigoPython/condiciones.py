#condicional if
x = 10
y = 50

#podemos usar operadore de comparacion(==,!=,>,<,>=,<=)

#siemple if

if x > y: 
	print('{0} es mas grande que {1}'.format(x,y)) 
else:
	print('{0} es mas grande que {1}'.format(y,x)) 

print("--------------------------")

if x < y:
	print('{0}es menor que {1}'.format(x,y))
elif x==y:
	print('{0} y {1} son iguales'.format(x,y))
else: 
	print('{0} es menor que{1}'.format(y,x))

#if anidados

if x > 2:
   if x <= 10:
	print('{0} es mas grande que 2 e igual/ menor a 10'.format(x))

#operaciones logicas(and, or, not)

#and
if x > 2 and x <= 10:
	print('{0}es mas grande que 2 e igual/menor a 10'.format(x))

#or
if x< 2 or x <=10:
	print('{0}es mas grande que 2 e igual/menor a 10'.format(x))

#not
if not(x==y):
	print('{0} no es igual a {1}'.format(x,y))
	
