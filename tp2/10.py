'''
10. Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los elementos de la 
primera que sean impares. El proceso deberá realizarse utilizando listas por comprensión. Imprimir las 
dos listas por pantalla.

'''
from random import randint

def Main():
    list_random = [ randint(1,100) for i in range(10)]
    list_random_odd = [ n for n in list_random if n%2!=0]
    print(list_random)
    print(list_random_odd)

if __name__ == '__main__':
    Main()