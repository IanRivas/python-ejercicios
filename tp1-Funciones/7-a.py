'''
Escribir una funcion diasiguiente(...) que reciba como parametro una fecha cualquiera
expresada por tres enteros (correspondientes al dia, mes y año) y calcule y devuelva 
tres enteros correspontientes el dia siguiente al dado
Utilizando esta funcion, desarrollar programas que permitan:

a. Sumar N dias a una fecha.
b. Calcular la cantidad de dias existentes entre dos fechas cualquiera.

'''

def SumarDias(dia, mes, año, dias):
    for i in range(0,dias):
        dia,mes,año = DiaSiguiente(dia,mes,año)
    print('Dia: ',dia,'/',mes,'/',año)

def DiaSiguiente(dia, mes, año):
    meses = [31,28,31,30,31,30,31,31,30,31,30,31]
    diasDelMes = meses[(mes-1)]
    if(dia == diasDelMes):
        if mes == 12:
            return 1,1,año+1
        else:
            return 1, mes+1, año
    else:
        return dia+1,mes,año
        
def Main():
    dia = int(input('Dia: '))
    mes = int(input('Mes: '))
    año = int(input('Año: '))
    dias = int(input('Cuantos dias le queres sumar?: '))
    SumarDias(dia,mes,año,dias)
    
if __name__ == '__main__':
    Main()