'''
Desarrollar una funcion que reciba tres numeros positivos y devuelva el mayor de los tres, solo si 
este es unico ( mayor estricto ). en caso de no existir el mayor estricto devolver -1. No utilizar 
operadores logicos (and, or, not). Desarrollar tambien un programa para ingresar los tres valores, 
incocar a la funcion y mostrar el maximo hallado, o un mensaje informativo si este no existe
'''

def CompararNumeros(N,N2):
    if(N > N2):
        return N
    elif(N == N2):
        return -1
    elif(N2 > N):
        return N2

def MayorEstricto(n1, n2, n3):
    mayor = CompararNumeros(n1,n2)
    if(mayor > 0):
       mayor = CompararNumeros(mayor,n3)
    else:
       mayor = CompararNumeros(n1,n3)
       if(n1 == mayor):
           return -1
    return mayor


def Main():
    n1 = int(input('Ingrese el primer numero: '))
    n2 = int(input('Ingrese el segundo numero: '))
    n3 = int(input('Ingrese el tercer numero: '))
    print(MayorEstricto(n1,n2,n3))

if __name__ == '__main__':
    Main()