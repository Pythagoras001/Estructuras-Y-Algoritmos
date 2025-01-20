lista = list(map(int, input().split()))

inicia = 0
estados = dict()
maxestado = 0

for fin in range(len(lista)):
    estados[lista[fin]] = estados.get(lista[fin], 0) + 1

    while len(estados) > 2:
        estados[lista[inicia]] -= 1
        if estados[lista[inicia]] == 0:
            del estados[lista[inicia]]
        inicia += 1

    maxestado = max(maxestado, fin - inicia+1)

print(maxestado)