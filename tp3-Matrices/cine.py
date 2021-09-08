# Mostrar_butacas: recibe por parámetros la matriz de butacas, la recorre y muestra por pantalla las butacas y su estado
 
# Reservar: recibe por parámetros la matriz de butacas, la butaca que se quiera reservar y cambia el estado de la matriz si es posible reservar la butaca o da aviso si ya esta ocupada.
 
# Cargar_sala: recibe la matriz de butacas vacía y define las dimensiones y los estados de las butacas al recorrerla
 
# Butacasada, la recorre y devuelve la cantidad de butacas desocupadas.
 
# Butacas contiguas: recibe la matriz de butacas ya cargada y a medida que la va recorriendo cuanta la cantidad de butacas libres contiguas y  almacena su posición en tres variables.

from random import randint

#IVANA
def mostrar_butacas():
    pass

#ADRIAN
def reserva():
    pass

#NICOLAS
def cargar_sala(matriz):
    columnas = len(matriz)
    filas = len(matriz[0])
    for x in range(filas):
        for z in range(columnas):
            matriz[x][z] = randint(0,1)
    return matriz


#IAN
def butacas_libres():
    pass

#AXEL
def butacas_contiguas():
    pass

#IVANA
def main():
    pass

main()