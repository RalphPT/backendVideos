nombres = ['Eduardo', 'Julia', 'Raul', 'Pedro']

print(nombres[0])
for nombre in nombres:
    print(nombre)


texto = 'Hola, el día de hoy llegaré tarde'

for letra in texto:
    print(letra)

# si en el range no le indicamos el inicio, empezará del 0
for numero in range(10):
    print(numero)

print('----------')
for numero in range(5, 10):
    print(numero)

print('----------')
for numero in range(2, 20, 2):
    print(numero)

mes = 'julio'
while(mes != 'agosto'):
    print('no es agosto')
    break

edad = 9
if edad >= 18:
    print('Puede consumir alcohol')
elif edad > 10:
    print('No puede consumir alcohol, per sí caramelos')
else:
    print('No puede consumir absolutamente nada')