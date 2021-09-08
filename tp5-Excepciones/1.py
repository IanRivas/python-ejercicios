'''
1. Desarrollar una función para ingresar a través del teclado un número natural. La función rechazará cualquier ingreso inválido de datos utilizando excepciones 
y mostrará la razón exacta del error. Controlar que se ingrese un número, que ese número sea entero y que sea mayor que 0. Devolver el valor ingresado cuando éste
sea correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma.

'''

def Main():
    try:
       natural_number = int(input('Ingrese un numero entero y mayor a 0: '))    
       assert natural_number > 0 
    except ValueError:
        print('Ingresaste un numero incorrecto')
    except AssertionError:
        print('Ingresaste un numero menor a 0')
    else:
        print(natural_number)
        

if __name__ == '__main__':
    Main()