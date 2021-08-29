'''
11. Resolver el siguiente problema, diseñando las funciones a utilizar:
Una clínica necesita un programa para atender a sus pacientes. Cada paciente que ingresa se anuncia en
la recepción indicando su número de afiliado (número entero de 4 dígitos) y además indica si viene por 
una urgencia (ingresando un 0) o con turno (ingresando un 1). Para finalizar se ingresa -1 como número 
de afiliado. Luego se solicita:

a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de los pacientes atendidos 
por turno en el orden que llegaron a la clínica.

b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue atendido por turno y 
cuántas por urgencia. Repetir esta búsqueda hasta que se ingrese -1 como número de afiliado.

'''

def recepcion():
    list_urgencia = []
    list_turno = []
    nro_afiliado = 0
    urg_or_turn = 0

    while nro_afiliado != -1:
        nro_afiliado = int(input('Ingrese su numero de afiliado(-1 para salir): '))
        if nro_afiliado != -1:
            urg_or_turn = int(input('Viene por una urgencia(ingresando un 0) o con turno (ingresando un 1): '))
            if urg_or_turn == 0:
                list_urgencia.append(nro_afiliado)
            elif urg_or_turn == 1:
                list_turno.append(nro_afiliado)
    
    return list_urgencia, list_turno

def buscador(list_urgencia, list_turno):
    veces_urgencia = 0
    veces_turno = 0
    nro_afiliado = 0
    while nro_afiliado != -1:
        nro_afiliado = int(input('Ingrese el numero de afiliado a buscar(-1 para salir): '))
        veces_urgencia = list_urgencia.count(nro_afiliado)
        veces_turno = list_turno.count(nro_afiliado)
        print(f'El afiliado {nro_afiliado} ingreso por emergencia {veces_urgencia} veces y por turno {veces_turno} veces')

def Main():
    urgencia, turno = recepcion()
    print(urgencia)
    print(turno)
    buscador(urgencia, turno)

if __name__ == '__main__':
    Main()