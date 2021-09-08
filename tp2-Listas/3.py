'''
3. Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa 
desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista. 

'''
def printArray(arr):
    for i in range(len(arr) - 10,len(arr)):
        print(arr[i])

def cuadradoArray(finalNumber):
    arr = []
    for i in range(1, finalNumber+1):
        arr.append(i**2)
    return arr

def Main():
    finalNumber = int(input('Ingrese un numero final del array(mayor a 10): '))
    arrayLoaded = cuadradoArray(finalNumber)
    printArray(arrayLoaded)


if __name__ == '__main__':
    Main()