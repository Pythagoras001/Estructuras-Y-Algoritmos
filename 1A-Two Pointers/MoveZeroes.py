lista = list(map(int, input().split()))

cero = 0

for i in range(len(lista)):
    if lista[i] !=  0:
        lista[cero], lista[i] = lista[i], lista[cero]
        cero += 1

print(lista)
