'''
Desarrollar una funcion que reciba tres numeros enteros positivos y verifique si corresponden a una
fecha valida (dia, mes, año). Devolver True o False segun la fecha sea correcta o no. Realizar tambien
un programa para verificar el comportamiento de la funcion

'''

def RevisarFecha(n1, n2, n3):
    meses = [31,28,31,30,31,30,31,31,30,31,30,31]
    if(n1 > 0 and n1 <= meses[n2-1]):
        if(n2 > 0 and n2 <= 12):
            if(n3 > 0 and n3 <= 2021):
                return True
    return False

def Main():
    n1 = int(input('Ingrese el dia: '))
    n2 = int(input('Ingrese el mes: '))
    n3 = int(input('Ingrese el año: '))
    print(RevisarFecha(n1,n2,n3))

if __name__ == '__main__':
    Main()