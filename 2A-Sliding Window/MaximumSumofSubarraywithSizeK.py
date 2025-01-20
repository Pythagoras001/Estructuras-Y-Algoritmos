lista = list(map(int, input().split()))
conjun = int(input())

inicio = 0
estado = 0
maxsuma = 0

for fin in range(len(lista)):
    estado += lista[fin]

    if fin - inicio+1 == conjun:
        maxsuma = max(maxsuma, estado)
        estado -= lista[inicio]
        inicio += 1

print(maxsuma)