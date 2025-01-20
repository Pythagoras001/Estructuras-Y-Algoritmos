def puntoCorte(cant, corte, lista):
    if corte == 0:
        corte += 1

    iz = 0
    dere = cant-1

    while iz <= dere:
        mid = (iz + dere) // 2

        if lista[mid] < corte and lista[mid-1] >= corte:
            return (mid) 
        elif lista[mid] < corte:
            dere = mid - 1
        else:
            iz = mid + 1

    if lista[0] >= corte:
        return cant
    else:
        return 0

cant, corte = list(map(int, input().split()))
lista = list(map(int, input().split()))

print(puntoCorte(cant, lista[corte-1], lista))