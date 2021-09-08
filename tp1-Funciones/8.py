'''
La siguiente funcion permite averiguar el dia de la semana para una fecha determinada. La fecha se 
suministra en forma de tres parametros enteros y la funcion devuelve 0 para domingo, 1 para lunes,
2 para martes, etc. Escribir un programa para imprimir por pantalla el calendario de un mes completo
correspondiente a un mes y año cualquiera basandose en la funcion suministrada. Considerar que la semana
comienza en domingo.

'''

def calendario(mes, año):
    'Imprime un calendario'
    meses = [31,28,31,30,31,30,31,31,30,31,30,31]
    print('D  L  M  M  J  V  S')
    #      0  1  2  3  4  5  6
    #      7  8  9 10 11 12 13
    #     14 15 16 17 18 19 29
    #     30 31 32
    start = diadelasemana(1,mes,año)*3
    if start > 0:
        print(' ' * start,end='')
    for i in range(1, meses[mes-1]+1):
        dia = diadelasemana(i,mes,año)
        if i < 10: print( i,end='  ')
        elif i >= 10 : print(i,end=' ')

        if dia == 6: print('')
    print('')

def diadelasemana(dia,mes,año):
    'Pasandole una fecha me dice que dia cae'
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo)) % 7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def Main():
    mes = int(input('Mes: '))
    año = int(input('Año: '))
    calendario(mes, año)
    
if __name__ == '__main__':
    Main()