'''
1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento, imprimiendo la matriz 
luego de invocar a cada función:

a. Cargar números enteros en una matriz de N x N, ingresar datos desde teclado.
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como parámetro.
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo nú-mero se recibe como parámetro.
h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo una lista con los números de las mismas.
NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera sea el valor ingresado.

'''
from random import randint

def cargarMatriz():
    'Function A'
    n = int(input('Crear una matriz de N: '))
    matriz = []
    random_number = 0
    for f in range(n):
        matriz.append([])
        # creas un array vacio y con el for de abajo lo llenas
        for c in range(n):
            random_number = randint(1,100)
            matriz[f].append(random_number)
    print(matriz)
    return matriz

def ordenarMatriz(m):
    'Function B'
    for f in m:
        f.sort()
    print(m)

def intercambiarFilas(m):
    'Function C'
    fila1 = int(input('Fila para intercambiar: '))
    fila2 = int(input('Segunda Fila para intercambiar: '))
    m[fila1],m[fila2] = m[fila2],m[fila1]
    print(m)

def intercambiarColumnas(m):
    'Function D'
    f = int(input('Que fila queres modificar las columnas?: '))
    columnas1 = int(input('Columnas para intercambiar: '))
    columnas2 = int(input('Segunda Columnas para intercambiar: '))
    m[f][columnas2],m[f][columnas1] = m[f][columnas1],m[f][columnas2]
    print(m)

def transponerMatriz(m):
    'Function E'
    matrizT = []
    for i in range(0,len(m)):
        matrizT.append([])
        for t in range(0,len(m)):
            matrizT[i].append(m[t][i])
    print(matrizT)
    
def promedioDeFila(m):
    'Function F'
    fila = int(input('Fila para sacar promedio: '))
    promedio = int(sum(m[fila]) / len(m[fila]))
    print(promedio, '%')

def promedioColumnaElmImpar(m):
    'Function G'
    columna = int(input('Columna para sacar promedio: '))
    sumaImpar = 0
    for i in range(0, len(m)):
       if m[i][columna] % 2 != 0:
           sumaImpar += m[i][columna]
    promedio = int(sumaImpar / len(m))
    print(promedio, '%')


def Main():
    matriz = cargarMatriz()
    # ordenarMatriz(matriz)
    # intercambiarFilas(matriz)
    # intercambiarColumnas(matriz)
    # transponerMatriz(matriz)
    # promedioDeFila(matriz)
    promedioColumnaElmImpar(matriz)


if __name__ == '__main__':
    Main()