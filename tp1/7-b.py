# b. Calcular la cantidad de dias existentes entre dos fechas cualquiera.

def DiaSiguiente(dia, mes, año):
    'Conseguir la fecha siguiente'
    meses = [31,28,31,30,31,30,31,31,30,31,30,31]
    diasDelMes = meses[(mes-1)]
    if(dia == diasDelMes):
        if mes == 12:
            return 1,1,año+1
        else:
            return 1, mes+1, año
    else:
        return dia+1,mes,año

def ConseguirFecha():
    'Ingresar fechas'
    dia = int(input('Dia: '))
    mes = int(input('Mes: '))
    año = int(input('Año: '))
    return [dia, mes ,año]
        
def fechaMenor(fecha1, fecha2):
    'devolver que fecha es menor'
    if fecha1[2] > fecha2[2]:
        return [fecha2, fecha1]
    elif fecha1[2] < fecha2[2]:
        return [fecha1, fecha2]
    elif fecha1[2] == fecha2[2]:
        if fecha1[1] > fecha2[1]:
            return [fecha2, fecha1]
        elif fecha1[1] < fecha2[1]:
            return [fecha1, fecha2]
        elif fecha1[1] == fecha2[1]:
            if fecha1[0] > fecha2[0]:
                return [fecha2, fecha1]
            elif fecha1[0] < fecha2[0]:
                return [fecha1, fecha2]
            elif fecha1[0] == fecha2[0]:
                return 0

def CalcularDias(fecha, fechaMayor):
    'Calcular dias entre 2 fechas'
    countDias = 0
    flag = True
    while flag:
        if fecha[0] == fechaMayor[0] and fecha[1] == fechaMayor[1] and fecha[2] == fechaMayor[2]:
            flag = False
        fecha[0],fecha[1],fecha[2] = DiaSiguiente(fecha[0],fecha[1],fecha[2])
        countDias += 1
    return countDias

def Main():
    fecha1 = ConseguirFecha()
    print('Otra Fecha')
    fecha2 = ConseguirFecha()

    fechas = fechaMenor(fecha1, fecha2)
    if fechas == 0:
        print('Las Fechas son las mismas')
        return
    print(CalcularDias(fechas[0], fechas[1]), 'dias de diferencia entre las fechas')
    
if __name__ == '__main__':
    Main()