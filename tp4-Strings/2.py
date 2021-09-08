'''
2. Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la misma tiene 80 columnas.

'''

def Main():
    cad = input('meter una cadena y la centro: ')
    cad2 = cad.center(80,'-')
    print(cad2)

if __name__ == '__main__':
    Main()