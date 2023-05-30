# listas (arrays)
# ordenada: puedo acceder a sus elementos mediante su posición > SE PUEDEN MODIFICAR

meses = ['enero', 'febrero', 'marzo']
mezclada = ['eduardo', 10, 50.5, False]

print(mezclada)
print(meses[0])
# al usar valores negativos en la posicion de la lista estaré indicando que lo haré de manera inversa
print(meses[-1])
#desde la pos 1 hasta < 2
print(meses[1:3])
print(meses[:2])
print(meses[1:])
#añade un elemento al array
meses.append('abril')
print(meses)

# 1. usando el método remove
meses.remove('enero')
print(meses)

print('elimina y devuelve el valor quitado')
# 2. usando el pop además de eliminarla también devuelve el valor quitado
mes_eliminado = meses.pop(1)

print(mes_eliminado)
print(meses)

# 3. del sirve para eliminar variables y contenidos de la lista
del meses[0]
print(meses)

#la longitud siempre será la cantidad de elementos que hay en una colección de datos
print(len(meses))

# DICCIONARIOS
#pero el ordenamiento se hace mediante llaves y valores > SON ORDENADOS PERO POR SUS LLAVES
persona = {
    'nombre': 'eduardo',
    'edad': 80,
    'nacionalidad': 'Peruano',
    'soltero': True,
    'estatura': 1.92
}

print(persona['nombre'])
persona['fecha_nacimiento'] = 'agosto de 1970'
persona['nombre'] = 'Roberto'
print(persona)
print(persona.keys())
print(persona.values())

del persona['estatura']
print(persona)


# Conjuntos > colección de datos desordenada que una vez creada no se podrá acceder a sus elementos por sus posiciones > SON DESORDENADOS
alumnos = {'Eduardo', 'María', 'Luisa', 'Dante'}
alumnos.add('Roberto')
alumnos.remove('Eduardo')
print(alumnos)

print('María' in alumnos)


# Tuplas
# Es una colección de datos que una vez creada no se puede modificar > NO SE PUEDE MODIFICAR
conocimientos = ('Matematica', 'Comunicacion', 'Backend')
#print(conocimientos.append('Raz Mate'))
conocimientos[1] = 'Frontend'
conocimientos.pop(1)