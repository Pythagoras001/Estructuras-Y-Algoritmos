idiom, grupos, mensaje = list(map(int, input().split()))

lista = input().split()
indices = dict()

lista2 = list(map(int, input().split()))
precios = dict()

for i in range(1, idiom+1):
    indices[lista[i-1]] = i
    precios[i] = lista2[i-1]

for _ in range(grupos):
    conju = list(map(int, input().split()))
    if conju[0] != 1:
        minn = min([precios[char] for char in conju[1:]])
        for n in range(conju[0]):
            precios[conju[n+1]] = minn

mens = input().split()
s = 0

for pala in mens:
    s += precios[indices[pala]]

print(s)