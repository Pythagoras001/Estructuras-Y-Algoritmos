cant, como, dif = list(map(int, input().split()))
lista = sorted(list(map(int, input().split())))

c = 1
posi = []

for i in range(cant-1):
    if (lista[i+1] - lista[i]) > dif:
            c += 1
            posi.append((lista[i+1] - (lista[i]+1))//dif)

posi.sort()

for num in posi:
    como -= num
    if como >= 0:
        c -= 1
    else:
        break

print(c)