'''
5. Desarrolle un programa que permita realizar reservas en una sala de cine de barrio de N filas con M butacas por cada fila. Desarrollar las siguientes 
funciones y utilizarlas en un mismo programa:

--mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas del cine por pantalla. Se deberá mostrar antes de que el usuario realice la 
    re-serva y se volverá a mostrar luego de la misma, con los estados actualizados.
--reservar: Deberá recibir una matriz y la butaca seleccionada, y actualizará la matriz en caso de estar disponible dicha butaca. La función devolverá True/False 
    si logró o no reservar la butaca.
--cargar_sala: recibirá una matriz como parámetro y la cargará con valores aleatorios para simular una sala con butacas ya reservadas.
--butacas_libres: Recibirá como parámetro la matriz y retornará cuántas butacas desocupadas hay en la sala.
--butacas_contiguas: Buscará la secuencia más larga de butacas libres conti-guas en una misma fila y devolverá las coordenadas de inicio de la misma.

'''

def butacas_libres_uno(m):
    'Calcula las butacas libres'
    butacas = 0
    for f in range(len(m)):
        for c in range(len(m[f])):
            if m[f][c] == 0:
                butacas += 1
    return butacas

def segunda_version(butacas,n,m):
    # use lambda
    liberados = 0
    for f in range(m):
        liberados += sum(butacas[f])
    return ((n*m)-liberados)

# def butacas_libres(butacas,n,m):
#      return (n*m) - sum([sum(butacas[f]) for f in range(n)])

butacas_libres = lambda butacas,n,m: (n*m) - sum([sum(butacas[f]) for f in range(n)])
  
def Main():
    matriz=[[1,0,0,1],[0,1,1,0],[0,0,0,0],[0,1,1,0]]
    print(butacas_libres(matriz,4,4))

if __name__ == '__main__':
    Main()