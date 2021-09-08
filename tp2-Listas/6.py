'''
6. Escribir una función que reciba una lista de números enteros como parámetros y la normalice, es decir
que todos sus elementos deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en 
la lista original. Desarrollar también un programa que permita verificar el comportamiento de la función.
Por ejemplo, normalizar([1,1,2]) debe devolver [0.25, 0.25, 0.50].

'''

def Normalize(arr):
    total = sum(arr)
    print(total)
    arrRes = []
    for i in arr:
        arrRes.append(round(i/total,2))
    return arrRes

def Main():
    arrExample = [1,1,2,8]
    print(Normalize(arrExample))

if __name__ == '__main__':
    Main()