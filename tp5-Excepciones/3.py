'''
3. Desarrollar una función que devuelva una cadena de caracteres con el nombre del mes cuyo número se recibe como parámetro. Los nombres de los meses deberán 
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función. Devolver una cadena vacía si el número de mes es inválido. La detección de meses 
inválidos deberá realizarse a través de excepciones.

'''

def mes(numMes):
    meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    try:
        assert numMes > 0
        mes = meses[numMes-1]
    except (ValueError, IndexError, AssertionError):
        return []
    else:
        return mes

def Main():
    numMes = int(input('ingrese el numero del mes: '))
    print(mes(numMes))

if __name__ == '__main__':
    Main()