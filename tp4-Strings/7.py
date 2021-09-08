'''
7. Escribir una función para eliminar una subcadena de una cadena de caracteres, a partir de una posición y cantidad de caracteres dadas, 
devolviendo la cadena resul-tante. Escribir también un programa para verificar el comportamiento de la misma. Escribir una función para cada uno
de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas

'''

def extraer_subcadena(cad, pos, cant):
    cad = list(cad)
    cad[pos:pos+cant] = []
    return "".join(cad)


def Main():
    cadena = "El número de teléfono es 4356-7890"
    print(extraer_subcadena(cadena, 25, 9))

if __name__ == '__main__':
    Main()