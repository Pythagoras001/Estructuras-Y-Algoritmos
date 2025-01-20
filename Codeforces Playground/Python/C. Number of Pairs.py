for _ in range(int(input())):
    n, l, r = map(int, input().split())
    lista = sorted(list(map(int, input().split())))

    ini = 0
    fin = n-1
    aws = 0

    while ini != fin:
        
        if lista[fin]+lista[ini] > r:
            fin -= 1
        
        elif lista[ini] + lista[fin] >= l:
            # Encontramos maximo
            iz = ini
            der = fin-1
            maxx = ini

            while iz <= der:
                mid = (iz + der)//2
                op = lista[mid] + lista[fin]

                if op <= r:
                    maxx = mid
                    iz = mid+1
                elif op > r:
                    der = mid-1

            aws += (maxx+1) - ini
            fin -= 1

        else:
            # Encontramos minimo
            ini += 1

    print(aws)