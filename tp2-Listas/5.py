'''
5. Escribir una función que reciba una lista como parámetro y devuelva True si la lista está ordenada 
en forma ascendente o False en caso contrario. Por ejemplo, ordenada([1,2,3]) retorna True y ordenada
(['b'.'a']) returna False. Desarrollar además un programa para verificar el comportamiento de la función

'''

def isSort(arr):
    arr2 = arr.copy()
    arr2.sort()
    for i in range(0,len(arr)):
        if arr[i] != arr2[i]:
            return False
    return True

def Main():
    arrSort = [1,2,3,4,5]
    arrNotSort = ['b','a']
    print(isSort(arrSort))
    print(isSort(arrNotSort))

if __name__ == '__main__':
    Main()