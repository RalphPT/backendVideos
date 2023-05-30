try:
    #raise Exception('Error!!!!') #Error genérico
    int('12')
    division = 10 / 0
    print(division)
except ValueError:
    #Ingresará a este bloque de código si algo en el try terminó de manera abrupta
    print('Error al ejecutar el código')
except ZeroDivisionError:
    print('Error al dividir entre 0')
except:
    print('Error desconocido')
else:
    # Se ejecutará si nunca ingresó a un except, si todo fue exitoso
    print('Yo me ejecuto de manera exitosa')
finally: 
    # Si fue exitoso o no
    print('Yo me ejecuto si todo estuvo bien o no')

print('Soy otro código importante en el proyecto')