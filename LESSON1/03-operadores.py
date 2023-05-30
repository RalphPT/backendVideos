# Operadores ariméticos
edad1 =  10
edad2 = 30
# Suma (+)
print(edad1 + edad2)

# Resta (-)
print(edad1 - edad2)

# Multiplicación (*)
print(edad1 * edad2)

# División (/)
print(edad1 / edad2)

# Módulo (%) > resultado entero de la división
print(edad1 % edad2)

# Cociente (//)
print(edad1 // edad2)


# Operadores Asignación
# Asignación (=)
persona = 'Ximena'

# Incremento
edad1 += 1 # incrementamos el valor de la variable edad1 en una unidad

# Decremento
edad1 -= 1 # decrementamos el valor de la variable edad1 en una unidad

# Multiplicador
edad1 *= 2 # edad1 = edad1 * 2

# División
edad1 /= 2

# Potencia
edad1 **=3 # edad1 = edad1 * edad1 * edad1


# Operadores Comparación
persona1 = 'Eduardo'
persona2 = 'Juan'

# == > es igual que
# python no existe el triple igual ===
print(persona1 == persona2)

print(persona1 != persona2)

# < , > menor que | mayor que
print(10 > 20)
print(50 < 80)

# <=, >= menor o igual que | mayor o igual que
print(10 >= 10)

# Operadores Lógicos
edad_juan = 10
edad_jonathan = 15
edad_roxana = 18
edad_martina = 19
# and (y) &&
#               V                             V             > V
print((edad_jonathan > edad_juan) and (edad_martina > edad_roxana))
#               V                             F             > F
print((edad_jonathan > edad_juan) and (edad_roxana > edad_martina))
# or (o)
#               V                             F             > V
print((edad_jonathan > edad_juan) or (edad_roxana > edad_martina))