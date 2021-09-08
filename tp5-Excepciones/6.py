'''
6. El método index permite buscar un elemento dentro de una lista, devolviendo la posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se 
produce una excepción de tipo ValueError. Desarrollar un programa que cargue una lista con números enteros ingresados a través del teclado (terminando con -1) y 
permita que el usuario ingrese el valor de algunos elementos para visualizar la posición que ocupan, utilizando el método index. Si el número no pertenece a la lista
se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.

'''
from random import randint

def Main():
    list_random = [randint(1,100) for i in range(randint(1,20))]
    print(list_random)
    intentos = 0
    try:
        while intentos < 3:
            try:
                num = int(input('Que numero busca?: '))
                assert list_random.index(num) != -1
                print(f"El numero se encuentra en la posicion {list_random.index(num)}")
                break
            except (ValueError,AssertionError,IndexError):
                print('No se encuentra ese numero en la lista')
                intentos += 1
    except ValueError:
        return 0
if __name__ == '__main__':
    Main()