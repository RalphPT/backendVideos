class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        # para indicar que un atributo o metodo sea privado se le coloca doble sub guión antes del nombre
        self.__ganancia = self.precio * 0.3

    def mostrarGanancia(self):
        print('La ganancia es %s' % self.__ganancia)
        print('El IGV es {}'.format(self.__calcularIgv()))

    def __calcularIgv(self):
        return self.precio * 0.18

producto1 = Producto('detergente', 7.50)
producto2 = Producto('shampoo', 18.40)
# podrá ser a'accedido' (no dara ningún error pero no hará caso alguno)
producto1.__ganancia = 100000
producto1.mostrarGanancia()
producto2.mostrarGanancia()
# no se puede acceder a un método privado de sde afuera de la clase
# product1.__calcularIgv()