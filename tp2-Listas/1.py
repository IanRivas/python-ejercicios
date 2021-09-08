'''
1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar 
su funcionamiento imprimiendo la lista luego de invocar a cada function:

a- Cargar una lista con números al azar de cuatro digitos. La cantidad de elementos también será un 
número al azar de dos dígitos.
b- Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
c- Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa 
desde el teclado y la función lo recibe como parámetro.
d-Determinar si el contenido de una lista cualquiera es capicua, sin usar listas auxiliares. 
Un ejemplo de lista capicua es [50,17,91,17,50]

'''
from random import randint

def LoadArray():
    'Function A'
    arrLength = randint(10,99)
    print('largo del array: ', arrLength)
    arr = []
    for i in range(0,arrLength - 1):
        randomNumber = randint(1000,9999)
        arr.append(randomNumber)
    print(arr)
    return arr

def SumArray(arr):
    'Function B'
    return sum(arr)

def DeleteFromArray(delNum, arr):
    'Function C'
    length = arr.count(delNum)
    for i in range(0,length):
        arr.remove(delNum)
    print(arr)

def CapicuaArray(arr):
    'Function D'
    length = len(arr)
    for i in range(0,int(length/2)):
        if(arr[i] != arr[length - i -1]):
            return False
    return True

def Main():
    loadedArr = LoadArray()
    print('La suma del array: ',SumArray(loadedArr))
    deleteNumber = int(input('Valor a eliminar: '))
    DeleteFromArray(deleteNumber,loadedArr)
    print(CapicuaArray(loadedArr))


if __name__ == '__main__':
    Main()
