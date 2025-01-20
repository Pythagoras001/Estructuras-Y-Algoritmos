veces = int(input())
lista = list(map(int, input().split()))
u = lista[0]

c = 0
for i in range(1, veces):
    if u > lista[i]:
        c += u - lista[i]
    else:
        u = lista[i]

print(c)