'''
Un comercio de electrodomesticos necesita para su linea de cajas un programa que le indique al cajero
el cambio que debe entregarle al cliente. Para eso se ingresan dos numeros enteros, correspondientes al 
total de la compra y al dinero recibido. Informar cuantos billetes de cada denominacion deben set 
entregados al cliente como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que 
existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error si el dinero recibido 
fuera insuficiente Ejemplo: si la compra es de $317 y se abona con $500, el vuelto debe contener 1 
billete de $100, 1 billete de $50, 1 billete de 20$, 1 billete de $10 y 3 billetes de $1.

'''
def imprimir(b, v):
    for i in range(0,7):
        if(v[i] != 0):
            print(v[i], 'billete de $', b[i])

def vuelto(compra, abona):
    if(abona < compra):
        print('Dinero Insuficiente')
        return 
    vueltoTotal = abona - compra
    billetes = [500, 100, 50, 20, 10, 5, 1]
    vueltoBilletes = []
    for i in billetes:
        res = int(vueltoTotal / i)
        vueltoBilletes.append(res)
        if res > 0:
            vueltoTotal = vueltoTotal - (res * i)
    imprimir(billetes, vueltoBilletes)

def Main():
    compra = int(input('Compra?: '))
    abona = int(input('Abona?: '))
    vuelto(compra, abona)

if __name__ == '__main__':
    Main()