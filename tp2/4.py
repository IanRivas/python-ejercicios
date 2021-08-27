'''
4. Eliminar de una lista de palabras las palabras que se encuentren en una segunda lista. Imprimir la 
lista original, la lista de palabras a eliminar y la lista resultante.

'''

def Main():
    listFruits = ['limon', 'manzana','naranja','manzana','banana', 'sandias','banana']
    listFruitsDelete = ['manzana', 'banana']
    listFruitsRes = listFruits.copy()
    index = 0
    for deleteFruit in listFruitsDelete:
        for fruit in listFruitsRes:
            if deleteFruit == fruit:
                listFruitsRes.pop(index)
            index += 1
        index = 0
    
    print(listFruits)
    print(listFruitsDelete)
    print(listFruitsRes)

if __name__ == '__main__':
    Main()