"""
Una suma de prefijo es una técnica para calcular
de manera eficiente la suma de submatrices en
una matriz de enteros.

Una vez que tenemos esas sumas de prefijos,
para calcular la suma de un subarreglo entre
los índices i y j , usamos la siguiente fórmula:
prefijo [ j + 1 ] - prefijo [ i ]  
"""

def prefix_sums(arr):
    n = len(arr)
    prefix = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + arr[i - 1]
    
    return prefix

a =prefix_sums([1,2,3,4,5,6])

print(a)
print(a[2 + 1] - a[1])