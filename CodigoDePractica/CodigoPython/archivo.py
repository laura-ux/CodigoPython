#crear archivo
miArchivo = open('miArchivo.txt','w')

#obtener informacion de ese archivo
print('Name: ', miArchivo.name)
print('Esta Cerrado: ', miArchivo.closed)
print('Esta Abierto: ',miArchivo.mode)

#Escribirle algo en el archivo
miArchivo.write('Hola python ')
miArchivo.close

#Agregar al archivo 
miArchivo = open('miArchivo.txt','a')
miArchivo.write(' hola c++')
miArchivo.close
