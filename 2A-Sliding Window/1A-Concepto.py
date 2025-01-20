"""
Considere utilizar el patrón de ventana deslizante para 
preguntas que implican la búsqueda de una subsecuencia 
continua en una matriz o cadena que satisfaga una determinada
restricción .

Si conoce la longitud de la subsecuencia que está buscando,
utilice una ventana deslizante de longitud fija. De lo contrario,
utilice una ventana deslizante de longitud variable.

Ejemplos:

-Encontrar la subcadena más grande sin repetir caracteres en una 
cadena dada (longitud variable).

-Encontrar la subcadena más grande que contiene un solo carácter 
que se puede formar reemplazando como máximo k caracteres en una
 cadena dada (longitud variable).

-Encontrar la suma más grande de una submatriz de tamaño k sin
elementos duplicados en una matriz dada (longitud fija).
"""

# Plantilla longitud variable 

def variable_length_sliding_window(nums):
    estado = dict() # Creamos un diccionario para almacenar los datos contados dentro de la ventana
    inicio = 0
    max_ = 0

    for end in range(len(nums)):
    # extender ventana
    # agrega nums[end] al estado en O(1) en el tiempo

        # while estado is not valid:
            # Si la ventana no es valida restamos el valor del inicio nums[start] 
            # y luego avanzamos q en el inicio
            inicio += 1

    # Guardamos que tipo de dato queremos guardar
    max_ = max(max_, end - inicio + 1)

    return max_

###############################################################################################

# Plantilla de logintud figa

def fixed_length_sliding_window(nums, k):
  state = 0 # Se define el estado
  start = 0
  max_ = 0

  for end in range(len(nums)):
    # Estiende la ventana se modifica el estado en una complejidad de O(1)
   
    if end - start + 1 == k:
      # Cuando pase lo que invalide la ventana guardamos el max
      # max_ = max(max_, contents of state)

      # Y acortamamos la ventana por atras

      start += 1

  return max_