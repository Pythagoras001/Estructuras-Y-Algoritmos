veces = int(input())

for _ in range(veces):
    cant, num = list(map(int, input().split()))
    lista = list(map(int, input().split()))

    s = 0
    maxx = -1

    for fin in range(cant):
        s += lista[fin]
        if s % num != 0:
            maxx = fin+1

    for ini in range(cant):
        s -= lista[ini]
        if s % num != 0:
            maxx = max(maxx, cant-(ini+1))

    print(maxx)



