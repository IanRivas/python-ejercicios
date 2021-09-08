'''
5. Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase y un entero N, y 
devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original. Escribir también un programa para verificar el
comportamiento de la misma. Hacer tres versiones de la función, para cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter

'''

def filtrar_palabras(palabras, N):
    return list(filter(lambda palabra: (len(palabra)>=N), palabras))

def filtrar_palabras_2(palabras, N):
    return [palabra for palabra in palabras if len(palabra)>= N]

def Main():
    frase = "devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original"
    palabras = frase.split(' ')
    print(filtrar_palabras(palabras,5))
    print(filtrar_palabras_2(palabras,5))

if __name__ == '__main__':
    Main()