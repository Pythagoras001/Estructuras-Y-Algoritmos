num = int(input())
lista = list(map(int, input().split()))

def rangoOptimo(num, lista):
    ini = 0
    estado =  {1:0, 0:0}
    s = lista.count(1)
    maxx = 0

    if s == num:
        return num-1
    
    for fin in range(num):
        estado[lista[fin]] += 1

        while estado[1] > estado[0]:
            estado[lista[ini]] -= 1
            ini += 1

        maxx = max((s-estado[1])+estado[0], maxx)

    return maxx

print(rangoOptimo(num, lista))
