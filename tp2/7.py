'''
7. Intercalar los elementos de una lista entre los elementos de otra. La intercalación deberá realizarse
exclusivamente mediante la técnica de rebanadas y no se creará una lista nueva sino que se modificará 
la primera. Por ejemplo, si lista1 = [8, 1, 3] y lista2 = [5, 9, 7], lista 1 deberá quedar como 
[8, 5, 1, 9, 3, 7].

'''

def intercalar(lista1,lista2):
    hasta=len(lista1) 
    for i in range(0,hasta):
        lista1[2*i+1:2*i+1]=lista2[i:i+1]
    # lista1[1:1] = lista2[0:1] [8,5,1,3]

def main():
    lista1=[8,1,3]
    lista2=[5,9,7]
    intercalar(lista1,lista2)
    print(lista1)


if __name__ == '__main__':
    main()