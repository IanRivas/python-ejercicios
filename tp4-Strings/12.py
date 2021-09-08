'''
12. Escribir un programa para crear una lista por comprensión con los naipes de la baraja española. La lista debe contener cadenas de caracteres. 
Ejemplo: ["1 Oros", "2 Oros"... ]. Imprimir la lista por pantalla.

'''

def Main():
    palos = ["Oro", "Espada", "Palo", "Copa"]
    mazo = [[f"{n} {p}" for n in range(1,13)]for p in palos]
    mazo.append(["Comodin","Comodin"])
    print(mazo)

if __name__ == '__main__':
    Main()