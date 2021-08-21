'''
Resolver el siguiente problema diseñando y utilizando funciones:

Un productor frutihorticula desea contabilizar sus cajones de naranjas segun el peso para poder cargar
el camion de reparto. La empresa cuenta con N camiones, y cada uno puede transportar hasta media 
tonelada(500 kilogramos). En un cajon caben 100 naranjas con un peso entre 200 y 300 gramos cada una.
Si el peso de alguna naranja se encuentra fuera del rango indicado, se clasifica para procesar como
jugo. Se solicita desarrollar un programa para ingresar la cantidad de naranjas cosechadas e informar 
cuantos cajones se pueden llenar, cuantas naranjas son para jugo y si hay algun sobrante de naranjas
que deba considerarse para el siguiente reparto. Simular el peso de cada unidad generando un numero  
entero al azar entre 150 y 350.

Ademas, se desea saber cuantos camiones se necesitan para transportar la cosecha, considerando que la 
ocupacion del camion no debe ser inferior al 80%; en caso contrario el camion no seran despachado por
su alto costo.

'''
from random import randint

def camionesCounter(peso):
    camiones = 0
    flag = True
    while flag:
        if peso >= 500000:
            peso -= 500000
            camiones += 1
        elif peso >= 400000:
            camiones += 1
            flag = False
        else:
            flag = False
    return camiones

def llenarCaja(naranjasTotal):
    caja = []
    cajasCounter = 0
    naranjasJugo = 0
    peso = 0
    while(naranjasTotal > 0):
        naranja = randint(150, 350)
        naranjasTotal -= 1
        if(naranja < 200 or naranja > 300):
            naranjasJugo += 1
        elif naranja >= 200 and naranja <= 300:
            caja.append(naranja)

        if len(caja) == 99:
            cajasCounter += 1
            peso += sum(caja)
            caja = []
    print(peso)
    return len(caja), cajasCounter, naranjasJugo, peso

def Main():
    naranjas = int(input('Naranjas: '))
    caja, cajasCounter, naranjasJugo, peso = llenarCaja(naranjas)
    camiones = camionesCounter(peso)
    print('Cantidad de cajas que podemos llegar: ', cajasCounter)
    print('Naranjas para jugo: ', naranjasJugo)
    print('Sobrante de naranjas: ', caja)
    print('Camiones necesarios para transportar la cosecha ',camiones )

if __name__ == '__main__':
    Main()