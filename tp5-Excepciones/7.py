'''
7. Escribir un programa que juegue con el usuario a adivinar un número. El programa debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo.
Para eso, cada vez que se introduce un valor se muestra un mensaje indicando si el nú-mero que tiene que adivinar es mayor o menor que el ingresado.
Cuando consiga adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar el número. Si el usuario introduce algo que no sea un número 
se mostrará un mensaje en pantalla y se lo contará como un intento más.

'''
from random import randint

def Main():
    randomNumber = randint(1,100)
    while True:
        try:
            number = int(input(f'Adivina el numero:{randomNumber} '))
            assert number == randomNumber
            print(f'Adivinaste el numero: {number}')
            break
        except (ValueError, AssertionError):
            if number < randomNumber:
                print('mas')
                continue
            elif number > randomNumber:
                print('menos')
                continue


if __name__ == '__main__':
    Main()