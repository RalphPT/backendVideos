class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludar(self):
        print('Hola soy {}'.format(self.nombre))

class Alumno(Usuario):
    def __init__(self, nombre, apellido, seguroMedico):
        # super()> sirve para pasar información a la clase de la cual estamos heredando
        super().__init__(nombre, apellido)
        self.seguroMedico = seguroMedico
usuario1 = Usuario('Juan', 'Martinez')
alumno1 = Alumno('Pedrito', 'Martinez', '123456')

usuario1.saludar()
alumno1.saludar()