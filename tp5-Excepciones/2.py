'''
2. Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, sume ambos valores y devuelva el resultado como un número real.
Devolver -1 si alguna de las cadenas no contiene un número válido, utilizando manejo de excepciones para detectar el error.

'''

def suma(a,b):
    try:
        res = int(a) + int(b)
    except ValueError:
        return -1
    return res
        
    

def Main():
    print(suma("hola","998"))

if __name__ == '__main__':
    Main()