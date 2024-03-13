import re

def es_nombre(palabra):
    # Este patrón de expresión regular verifica si la palabra contiene solo letras y tiene una longitud mínima
    patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]{2,}$'
    return re.match(patron, palabra)

def extraer_nombres(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r', encoding='utf-8') as entrada:
        with open(archivo_salida, 'w', encoding='utf-8') as salida:
            for linea in entrada:
                palabras = linea.split()
                for palabra in palabras:
                    if es_nombre(palabra):
                        salida.write(palabra + '\n')

archivo_entrada = 'Autores.txt'
archivo_salida = 'nombres.txt'
extraer_nombres(archivo_entrada, archivo_salida)

