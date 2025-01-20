lista = list(map(int, input().split()))

pila = []
base = [-1] * len(lista)

for i in range(len(lista)):
    while pila and lista[i] > lista[pila[-1]]:
        index = pila.pop()
        base[index] = lista[i]
    pila.append(i)

print(base)