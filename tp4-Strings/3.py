'''
3. Los números de claves de dos cajas fuertes están intercalados dentro de un nú-mero entero llamado "clave maestra", cuya longitud no se conoce. 
Realizar un pro-grama para obtener ambas claves, donde la primera se construye con los dígitos ubicados en posiciones impares de la clave maestra y 
la segunda con los dígitos ubicados en posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave maestra fuera 18293, 
la clave 1 sería 123 y la clave 2 sería 89.

'''

#18293 - 123 - 89
def Main():
    codigo = input('ingrese la clave maestra: ')
    clave1 = ''
    clave2 = ''
    for i in range(0,len(codigo),2):
        clave1 += codigo[i]
    for i in range(1,len(codigo),2):
        clave2 += codigo[i]
    print(f'Clave 1 es {clave1}')
    print(f'Clave 2 es {clave2}')
    


if __name__ == '__main__':
    Main()