'''
10. Desarrollar una función para reemplazar todas las apariciones de una palabra por otra en una cadena de caracteres y devolver la cadena obtenida y 
un entero con la cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse palabras completas, y no fragmentos de palabras. 
Escribir también un programa para verificar el comportamiento de la función.

'''

def replace_gappy(cad, palabra_borrar, palabra_nueva):
    cad = cad.split()
    cad_remplazo = []
    count = 0
    for p in cad:
        if p == palabra_borrar:
            cad_remplazo.append(palabra_nueva)
            count += 1
        else:
            cad_remplazo.append(p)
    return count, " ".join(cad_remplazo)


def Main():
    cad = "Desarrollar una función para reemplazar todas las apariciones de una palabra por otra en una cadena de caracteres y devolver la cadena obtenida"
    palabra1 = "cadena"
    palabra2 = "string"
    count_reemplazos, cad_remplazado = replace_gappy(cad,palabra1, palabra2)
    print(f"la palabra {palabra1} se reemplazo {count_reemplazos} veces por {palabra2}")
    print(cad_remplazado)

if __name__ == '__main__':
    Main()