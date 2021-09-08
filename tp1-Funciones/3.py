'''
Una persona desea llevar el control de los gastos realizados al viajar en el subterraneo dentro 
de un mes. Sabiendo que dicho medio de transporte utiliza un esquema de tarifas deccrecientes
(detalladas en la tabla de abajo) se solicita desarrollar una funcion que reciba como parametro la cantidad
de viajes realizados en un determinado mes y devuelva el total gastado en viajes. Realizar tambien un 
programa para verificar el comportamiento de la funcion
1-20  30$
21-30 20% descuento al total
31-40 30% descuento al total
mas de 40 40% descuento al total

'''
def calculadorGastos(viajes):
    precio = 30
    total = viajes * precio
    if(viajes > 0 and viajes <= 20):
        return total
    elif(viajes >= 21 and viajes <= 30):
        return total - (total * 0.2)
    elif(viajes >= 31 and viajes <= 40):
        return total - (total * 0.3)
    elif(viajes > 40):
        return total - (total * 0.4)


def Main():
    cantidadDeViajes = int(input('Cantidad de viajes realizados?: '))
    print(int(calculadorGastos(cantidadDeViajes)),'$',sep='')

if __name__ == '__main__':
    Main()