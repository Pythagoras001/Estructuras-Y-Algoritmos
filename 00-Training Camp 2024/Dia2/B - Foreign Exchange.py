while True:
    veces = int(input())

    if veces == 0:
        break

    dicc = dict()
    r = 'YES'
    c = 0
    c1 = 0

    for _ in range(veces):
        sitio, destino = input().split()

        if dicc.get(destino+sitio, 'a') == 'a':
            dicc[sitio+destino] = 1
            c1 += 1
        else:
            c += 1

    if c != c1: r = 'NO'
    print(r)