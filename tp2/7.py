'''
7. Intercalar los elementos de una lista entre los elementos de otra. La intercalación deberá realizarse
exclusivamente mediante la técnica de rebanadas y no se creará una lista nueva sino que se modificará 
la primera. Por ejemplo, si lista1 = [8, 1, 3] y lista2 = [5, 9, 7], lista 1 deberá quedar como 
[8, 5, 1, 9, 3, 7].

'''

def Main():
    lista1 = [8, 1, 3]
    lista1[0::0] = [5, 9, 7]
    print(lista1)

if __name__ == '__main__':
    Main()