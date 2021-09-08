'''
5. La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del módulo math. Escribir un programa que utilice esta función para calcular la raíz cuadrada 
de un número cualquiera ingresado a través del teclado. El programa debe utilizar manejo de excepciones para evitar errores si se ingresa un número negativo.

'''

from math import sqrt

def Main():
    try:
        num = int(input('ingrese un numero para hacerle la raiz: '))
        assert num >= 0
    except (ValueError, AssertionError):
        print('Numero invalido , tiene que ser mayor a 0')
    else: 
        print(sqrt(num))

if __name__ == '__main__':
    Main()