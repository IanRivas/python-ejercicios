'''
2. Escribir funciones para:
a. Generar una lista de 50 números aleatorios del 1 al 100.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido.
   La función no debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista
   original, sin importar el orden.
Combinar estas tres funciones en un mismo programa.

'''
from random import randint

def LoadArray():
   'Function A'
   arr = []
   for i in range(0,50):
      randomNum = randint(1,100)
      arr.append(randomNum)
   return arr

def hasRepeatNumber(arr):
   'Function B'
   for i in arr:
      if arr.count(i) > 1:
         print(i,' esta repetido en el array.')
         return True
   return False

def getNoRepeatNumberArray(arr):
   'Function C'
   noRepeatArray = []
   for i in arr:
      if arr.count(i) == 1:
         noRepeatArray.append(i)
   return noRepeatArray

def Main():
   loadedArray = LoadArray()
   print(loadedArray)
   print(hasRepeatNumber(loadedArray))
   print(getNoRepeatNumberArray(loadedArray))


if __name__ == '__main__':
    Main()