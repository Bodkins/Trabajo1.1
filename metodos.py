import os
from time import sleep

from ciudades import ciudades 

# Indexación de ciudades.
indices = [*ciudades]

# Métodos
clear = lambda: os.system('cls')
clear()

def imprimirCiudades():
    print('Lista de ciudades: ')
    for key in indices:
        print('>>> ' + key)
    print('')


def seleccionDeCiudadInicial():
    imprimirCiudades()
    # Se pide la ciudad inicial.
    start = input('Ciudad inicial: ')
    return start



def busquedaDeCiudad(start):
    # Variables adicionales.
    indice = 0
    isCityFounded = False

    # se empieza la búsqueda de la ciudad dentro de las ciudades guardadas en "indices", variable con datos provenientes de "ciudades"
    for key in indices:
        if indices[indice] == start:
            start = indice
            isCityFounded = True
            break
        else:
            indice = indice + 1

    # Se validad si la ciudad ha sido encontrada.
    if isCityFounded:
        print('¡La ciudad ha sido seleccionada con éxito!')
    else:
        print('Parece que la ciudad solicitada no ha sido encontrada...')
        sleep(2)
        clear()
        print('--- Intenta de nuevo ---')
        busquedaDeCiudad(seleccionDeCiudadInicial())

ciudadesVisitadas = []

i = 0

def encontrarVecinoMasCercano(ciudadEnCuestion):
    
    if ciudadesVisitadas.count == indices.count:
        endPrograma()

    for key in indices:
        if ciudadEnCuestion == i:
            encontrarVecinoMasCercano(ciudadEnCuestion)
        elif ciudades[indices[0]][indices[3]]:
            # Algo de aqui para implementar si 
            # https://www.mclibre.org/consultar/python/lecciones/python-for-2.html
            print()

def endPrograma():
    # Imprimir resultados
    print('xd')