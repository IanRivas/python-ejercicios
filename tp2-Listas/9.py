'''
9. Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 que no sean múltiplos
 de 5. A y B se ingresar desde el teclado.

'''

def Main():
    a = int(input('Ingrese un numero:'))
    b = int(input('Ingrese un segundo numero:'))
    listaFinal = [i for i in range(a,b) if i%7==0 and i%5!=0]
    print(listaFinal)

if __name__ == '__main__':
    Main()