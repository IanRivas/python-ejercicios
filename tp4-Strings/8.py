'''
8. Escribir una función que reciba como parámetro una cadena de caracteres en la que las palabras se encuentran separadas por uno o más espacios.
Devolver otra cadena con las palabras ordenadas alfabéticamente, dejando un espacio entre cada una.

'''

def ordenar_cad(cad):
    palabras = cad.split()
    palabras.sort()
    return " ".join(palabras)
    

def Main():
    cad = "escribir una función que reciba como  parámetro una cadena de  caracteres en la que las palabras  se encuentran separadas por uno o más espacios"
    print(ordenar_cad(cad))

if __name__ == '__main__':
    Main()