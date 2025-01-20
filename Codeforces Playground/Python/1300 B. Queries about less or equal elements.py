a, b = list(map(int, input().split()))
lista1 = sorted(list(map(int, input().split())))
lista2 = list(map(int, input().split()))

def busqueda(i):
    if lista2[i] >= lista1[-1]:
        return a
    elif lista2[i] < lista1[0]:
        return 0
    
    iz = 0
    dere = a-1

    while iz <= dere:
        mid = (iz + dere) // 2
        
        if lista1[mid-1] <= lista2[i] and lista1[mid] > lista2[i]:
            return mid
            
        elif lista1[mid] <= lista2[i]:
            iz = mid + 1

        else:
            dere = mid - 1

for i in range(b):
    print(busqueda(i), end=' ')