class Estudiante(object):
    def estudiante(self):
        print("el estudiante es {}".format(self.nombre))


class Persona(Estudiante):
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def impresion(self):
        print('Hola soy {} y tengo {} años'.format(self.nombre, self.edad))


nico = Persona('Nicolas',22,'masculino')
nico.impresion()
nico.estudiante()