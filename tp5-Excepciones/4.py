'''
4. Todo programa Python es susceptible de ser interrumpido mediante la pulsación de las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt.
Reali-zar un programa para imprimir los números enteros entre 1 y 100000, y que solici-te confirmación al usuario antes de detenerse cuando se presione Ctrl-C.

'''

def Main():
    for i in range(1,100001):
        try:
            print(i)
        except KeyboardInterrupt:
            res = input('Detenemos impresion?(y/n)')
            if res == 'y' or res == 'Y':
                return 0

if __name__ == '__main__':
    Main()