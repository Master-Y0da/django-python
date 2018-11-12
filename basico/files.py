archivo = open('prueba.txt','w')
archivo.write('creando una mejor version de mi \n soy maquina!!')
archivo.close()

lectura = open('prueba.txt','r+')
a = lectura.read()
print(a)
lectura.close()