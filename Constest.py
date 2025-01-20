cant = int(input())
g = int(input())
p = int(input())

juegos = [[0, 0] for _ in range(cant)]

v1 = 0
v2 = -1
c = 0

for i in range(cant-1):
    if g > 0:
        juegos[i][0] = 1
        g -= 1
        v1 = i
    elif p > 0:
        juegos[i][1] = 1
        p -= 1
        v2 = i

    if juegos[i][0] == juegos[i][1]:
        c += 1

juegos[v1][0] += g
juegos[-1][1] += p

if juegos[-1][0] == juegos[-1][1]:
        c += 1

print(c)
for x, y in juegos:
    print(f'{x}:{y}')