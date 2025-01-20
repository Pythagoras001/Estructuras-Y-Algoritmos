veces = int(input())

for _ in range(veces):
    segu, vida = list(map(int, input().split()))
    lista = list(map(int, input().split()))

    r = vida
    iz = 1
    dere = vida-1

    while iz <= dere:
        mid = (iz + dere) // 2
        a = vida-mid

        for i in range(segu-1):
            if a <= 0:
                break
            a -= min(lista[i+1]-lista[i], mid)
        
        if a <= 0:
            dere = mid - 1
            r = min(mid, r)

        elif a > 0:
            iz = mid + 1

    print(r)