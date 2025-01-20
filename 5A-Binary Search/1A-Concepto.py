"""
La búsqueda binaria es un algoritmo eficaz porque nos permite
reducir repetidamente nuestro espacio de búsqueda a la mitad 
hasta que encontremos el objetivo o concluyamos que no está
en la matriz . En otras palabras, durante cada iteración del
algoritmo, podemos descartar la mitad del espacio de búsqueda.
"""

def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1 

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return True
    
    return False

lista = list(map(int, input().split()))
num = int(input())

print(binarySearch(lista, num))

