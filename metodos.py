import os
import array
from time import sleep
from typing import Counter

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
            city=key
            
            isCityFounded = True
            break
        else:
            indice = indice + 1

    # Se validad si la ciudad ha sido encontrada.
    if isCityFounded:
        print('¡La ciudad ha sido seleccionada con éxito!')
        encontrarVecinoMasCercano(city)
    else:
        print('Parece que la ciudad solicitada no ha sido encontrada...')
        sleep(2)
        clear()
        print('--- Intenta de nuevo ---')
        busquedaDeCiudad(seleccionDeCiudadInicial())

ciudadesVisitadas = []
ciudadesMenores = []
valor = 0
i = 0

def encontrarVecinoMasCercano(ciudadEnCuestion):
    
    if ciudadesVisitadas.count == indices.count:
        endPrograma()

    for key in indices:
        valCiud=[*ciudades[ciudadEnCuestion].values()]
        ciud=[*ciudades[ciudadEnCuestion]]
        #print(ciud)
        #print(valCiud)
        if ciudadEnCuestion != i:
            
            # Algo de aqui para implementar si 
            #ciudadesElegir = indices[key]
            if len(ciudadesVisitadas)==0:
                ciudadesVisitadas.append(ciudadEnCuestion)
                ciudadesMenores= sorted(ciudades[ciudadEnCuestion].values())
                inde=0
                iv=0
                ii=0
                
                while inde<=len(ciudadesMenores):
                    
                    while ciudadesMenores[iv]!= valCiud[inde]:
                        inde=inde+1
                        while ii<len(ciudadesVisitadas):
                         entra = False
                         if ciud[inde]==ciudadesVisitadas[ii]:
                           entra=True
                           valor=valor+valCiud[inde]
                           ciudadEnCuestion=ciud[inde]
                           ciudadesVisitadas.append(ciudadEnCuestion)
                           print(ciudadEnCuestion)
                           print(valor)
                           encontrarVecinoMasCercano(ciudadEnCuestion)
                        ii=ii+1
                    iv=iv+1
                
                inde=inde+1
                
                #print(ciudades[key])
            elif  ciudades[indices[0]][indices[3]]:
                endPrograma()
            #ciudadesVisitadas.append(ciudadEnCuestion)
            # https://www.mclibre.org/cciudades[indices[0]][indices[3]]:onsultar/python/lecciones/python-for-2.html

            #print(ciudadesVisitadas[0])
            #print(len(ciudades))

def endPrograma():
    # Imprimir resultados
    print(valor)