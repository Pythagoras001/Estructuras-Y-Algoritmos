veces = int(input())

for _ in range(veces):
    num = int(input())
    lista = list(map(int, input().split()))

    s = 0
    minn = 0
    maxx = 0

    for i in range(num):
        if lista[i] < 0:
            if minn == 0:
                minn = lista[i]

            minn = max(minn, lista[i])
            s += maxx
            maxx = 0
        else:
            maxx = max(maxx, lista[i])
            s += minn
            minn = 0

    print((s + minn + maxx))