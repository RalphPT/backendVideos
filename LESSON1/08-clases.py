# Una clase es una plantilla que puede ser utilizada N veces
class Persona:
    # Las variables que creemos dentro de una clase se pasan a llamar ATRIBUTOS
    fechaNacimiento = '1990-01-01'
    nombre = ''
    estatura = 1.50

    def saludar(self):
        # funciones definidas dentro de la clase pasan a llamarse METODOS
        # Todo METODO de una clase SIEMPRE llevará definido como primer parámetro el 'self' que sirve para hacer referencia ala funcionabilidad de la clase como sus atributos otros metodos, en otros lenguajes de programacion como C# o Java se utiliza el 'this'
        texto = 'Hola soy %s, mucho gusto' % self.nombre
        texto = 'Hola soy {}, mucho gusto'.format(self.nombre)
        texto = 'Hola soy ' + self.nombre + ', mucho gusto'
        print(texto)

    def despedir(self):
        print('Adioooooos')

# crear una instancia de una clase, es sacar una copia de esa clase y almacenarla en esa variable
persona1 = Persona()
persona2 = Persona()

persona1.nombre = 'Rigoberto'
persona2.nombre = 'Derrick'

persona1.saludar()
persona2.saludar()