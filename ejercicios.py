'''
 * Dado un array de enteros ordenado y sin repetidos,
 * crea una función que calcule y retorne todos los que faltan entre
 * el mayor y el menor.
 * - Lanza un error si el array de entrada no es correcto.
'''

lista_numeros = [2, 5, 8, 10, 12]

def tiene_valores_repetidos(numeros: list) -> bool:
    for numero in numeros:
        if numeros.count(numero) > 1:
            return True
    return False

def solo_valores_enteros(numeros) -> bool:
    for numero in numeros:
        if type(numero) != int:
            return False
    return True  

def esta_ordenado(numeros) -> bool:
    pass

def numeros_perdidos(numeros):
    lista_numeros_perdidos = []
    for i in range (numeros[0], numeros[-1]+1):
        if i in numeros:
            pass
        else:
            lista_numeros_perdidos.append(i)
    return (lista_numeros_perdidos)
        

print(tiene_valores_repetidos(lista_numeros))
print(solo_valores_enteros(lista_numeros))
print(numeros_perdidos(lista_numeros))
