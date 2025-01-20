veces = int(input())

for _ in range(veces):
    cant, suma = list(map(int, input().split()))
    lista = list(map(int, input().split()))

    ini = 0
    s = 0
    minn = cant

    for fin in range(cant):
        s += lista[fin]

        while s > suma:
            s -= lista[ini]
            ini += 1

        if s == suma:
            minn = min(minn, ini + (cant-(fin+1)))

    if minn == cant:
        minn = -1

    print(minn)

