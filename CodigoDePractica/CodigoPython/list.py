#lista numeros
numbers = [1,2,3,4,5]
frutas = ["manzanas","narnajas","peras","grapes"]

numbers2 = list((1,2,3,4,5))
print(numbers,frutas)

print(frutas[0])

print(len(frutas))

#agragar a la lista
frutas.append("Mangos")
print(frutas)

#remover de la lista
frutas.remove("grapes")
print(frutas)

#insertar position
frutas.insert(2,"fresas")
print(frutas)

#remove la posicion
frutas.pop(2)

#invertir la list
frutas.reverse()
print(frutas)

#sort alfabeticamente 
frutas.sort()
print(frutas)
