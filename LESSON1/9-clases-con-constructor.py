class Persona:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def saludar(self):
        text = 'Hola, soy {} y soy {}'.format(self.nombre, self.nacionalidad)
        print(text)

persona1 = Persona('Raul', 'Colombiano')
persona2 = Persona('Ximena', 'Uruguaya')

persona1.saludar()
persona2.saludar()