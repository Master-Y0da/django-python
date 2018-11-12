import random

opciones = {'1':{'choice': 'piedra','pierde':'papel'},'2':{'choice': 'papel','pierde':'tijera'},'3':{'choice': 'tijera','pierde':'piedra'}}
separador = '-' * 20

while(True):

    print(separador)
    hola = input('ingresa piedra papel o tijera \n')

    for key,valor in opciones:
        print(valor)
        if(hola in opciones[valor]['choice']):
            pc = random.choice(opciones[valor]['choice'])
            obj = opciones[valor]
            print("el pc eligio", pc)
            if(obj[valor]['choice']== hola):
                print("empate")
            if(obj[valor]['pierde'] == hola):
                print('Ganaste!!')
            else:
                print('perdiste')


print("hola")
print("el resultado es:", 4*3)


def algo(a):
    print(a)


algo(3)

if 'algo' == 'algoo':
    print("verdadero")
else:
    print("falso")

i = 0
rango = 10
resultado = 1
for i in range(1, rango+1):
    resultado *= i

print("el numero es -->", resultado)
