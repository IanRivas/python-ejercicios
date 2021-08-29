'''
12. Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se ingresa el número 
de socio de cinco dígitos hasta ingresar un cero como fin de car-ga. Se solicita:

a. Informar para cada socio, cuántas veces ingresó al club (cada socio debe aparecer una
 sola vez en el informe).
 
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus ingresos. Mostrar los 
registros de entrada al club antes y después de eliminarlo. Informar cuántos ingresos se eliminaron.

'''
def recepcion():
    'ingreso de socio al club'
    list_ingresos = [55678,99984,55678,12234,33687,64981,57798,11649]
    nro_socio = -1
   
    while nro_socio != 0:
        nro_socio = int(input('Ingrese su numero de socio(0 para salir): '))
        if 9999 < nro_socio <= 99999 :
            list_ingresos.append(nro_socio)

    return list_ingresos

def ingresos(list_ingresos):
    'Realiza informe de cuantas veces entro'
    list = []
    count = 0
    print('INFORME')
    for socio in list_ingresos:
        count = list_ingresos.count(socio)
        if socio not in list:
            print(f'El socio nro: {socio} ingreso {count} veces')
            list.append(socio)

def eliminarSocio(nro_socio, list):
    'elimina socio y te dice cuantas veces entro'
    count = 0
    for i in range(0,len(list)-1):
        print('HOOOOLA ' ,i)
        if nro_socio == list[i]:
            count += 1
            list.pop(i)
    return count, list

def Main():
    list_ingresos = recepcion()
    ingresos(list_ingresos)
    nro_socio_delete = int(input('ingresar numero de socio a eliminar: '))
    print('lista antes de eliminar')
    print(list_ingresos)
    print('lista de ingresos despues de eliminar')
    count_ingresos , list_ingresos = eliminarSocio(nro_socio_delete,list_ingresos)
    print(f'el socio {nro_socio_delete} se elimino {count_ingresos} ingresos del registro') 
    print(list_ingresos)

if __name__ == '__main__':
    Main()