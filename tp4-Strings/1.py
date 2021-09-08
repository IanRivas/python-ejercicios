'''
1. Desarrollar una función que determine si una cadena de caracteres es capicúa, sin utilizar cadenas auxiliares ni rebanadas. 
Escribir además un programa que permita verificar su funcionamiento.

'''

def Capicua(c):
    rev = -1
    isCapicua = True
    for i in range(0,int(len(c)/2)):
        if c[i] != c[rev]:
            isCapicua = False
        rev -= 1
    return isCapicua

def Main():
    cad = 'reconocer'
    print(Capicua(cad))

if __name__ == '__main__':
    Main()