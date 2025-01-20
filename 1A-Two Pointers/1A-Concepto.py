"""
La técnica de dos punteros aprovecha el hecho de que la matriz 
de entrada está ordenada para eliminar la cantidad de pares que
consideramos desde O(n^2 ) hasta O(n)

Considere utilizar la técnica de dos punteros para preguntas que
impliquen la búsqueda de un par (o más) de elementos en una matriz
que cumplan con ciertos criterios.
"""

def DosSuma(nums, target): 
  left, right = 0, len(nums) - 1 # Ponemos los punteros a los extremos de la lista que esta ordenada
      
  while left < right: # La izquierda simpre debe de estar ubicada antes que la derecha de lo contrario no exite tal suma
    current_sum = nums[left] + nums[right] # Realizamos la suma
    if current_sum == target: # Si la suma es igual al objetivo imprimimos los dos numeros que cumplen con esta suma y un True
        print( nums[left], nums[right])
        return True

    if current_sum < target: # Si la suma es menor al objetivo movemos el puntero izquierdo a la derecha para tener una suma mas alta
        left += 1
    else:
        right -= 1 # Si el la suma es mayor tendremos que mover el puntero derecho a la izquierda para tener una suma menor
      
  return False

resultado = DosSuma([1,2,3,4,5,6,7,8,10], 14) # Tenemos una lista ordenada de menor a mayor y el la suma que estamos buscando

print(resultado)