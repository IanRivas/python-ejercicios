'''
9. Desarrollar una función que devuelva una subcadena con los últimos N caracteres de una cadena dada. La cadena y el valor de N se pasan como parámetros.

'''

def extraer_subcadena(cad, cantidad):
    posicion_inicio = len(cad) -cantidad
    return cad[posicion_inicio:]


def Main():
    cadena = "El número de teléfono es 4356-7890"
    print(extraer_subcadena(cadena, 9))

if __name__ == '__main__':
    Main()