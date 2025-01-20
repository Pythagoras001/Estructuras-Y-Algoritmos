"""
Podemos pensar en un montón como una matriz con una propiedad especial:
el valor más pequeño de la matriz siempre está en el primer índice de
la matriz.

Si eliminamos el valor más pequeño del montón, los elementos de la 
matriz se reorganizan eficientemente para que el siguiente valor más
pequeño ocupe su lugar al principio de la matriz.

Los montones se utilizan con mayor frecuencia en entrevistas de codificación
para resolver una clase de problemas conocidos como problemas "Top K", que
implican encontrar los k elementos más pequeños o más grandes en una
colección de elementos.
"""

import heapq

arr = [3, 1, 4, 1, 5, 9, 2]

# convierte la matriz en un montón en el lugar. O(n)
heapq.heapify(arr)

# Empuja 0 al montón. O(log n)
heapq.heappush(arr, 0)

# mira el elemento mínimo = 0. O(1)
arr[0]

# pop y devuelve el elemento mínimo = 0. O(log n)
min_element = heapq.heappop(arr)

# echa un vistazo al nuevo elemento mínimo = 1. O(1)
arr[0]

print(arr)