'''
Escribir dos funciones separadas para imprimir por pantalla los siguientes patrones
de asteriscos, donde la cantidad de filas se recibe como parámetro:

  *******       **
  *******       ****
  *******       ******
'''

def cuadrado(filas):
    for i in range(0,filas):
        print('**********')

def triangulo(filas):
    str = '**'
    for i in range(0,filas):
        print(str)
        str += '**'

def Main():
    CoT = input('Cuadrado o Triangulo? (C/T): ')
    if('C'== CoT or 'c' == CoT):
        filas = int(input('Filas?: '))
        cuadrado(filas)
    elif('T'== CoT or 't' == CoT):
        filas = int(input('Filas?: '))
        triangulo(filas)
    else:
        print('Error al determinar cuadrado o triangulo')


if __name__ == '__main__':
    Main()