'''
8. Utilizar la técnica de listas por comprensión para construir una lista con todos los números 
impares comprendidos entre 100 y 200.

'''

def Main():
    listaFinal = [i for i in range(101,200,2)]
    print(listaFinal)

if __name__ == '__main__':
    Main()