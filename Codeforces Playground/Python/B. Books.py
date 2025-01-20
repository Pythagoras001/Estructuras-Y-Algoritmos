book, time = list(map(int, input().split()))
lista = list(map(int, input().split()))

ini = 0
maxx = 0
s = 0

for fin in range(book):
    s += lista[fin]

    while s > time:
        s -= lista[ini]
        ini += 1

    maxx = max(maxx, fin - ini+1)

print(maxx)