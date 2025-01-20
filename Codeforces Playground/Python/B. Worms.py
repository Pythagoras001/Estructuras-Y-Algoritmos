cant = int(input())
lista = list(map(int, input().split()))

prefix = [0] * (cant+1)

for i in range(1, cant+1):
    prefix[i] = prefix[i-1] + lista[i-1]

cantsele = int(input())
selecci = list(map(int, input().split()))

for worm in selecci:

    iz = 1
    dere = cant

    while iz <= dere:
        mid = (iz + dere) // 2

        if prefix[mid] >= worm and prefix[mid-1] < worm:
            print(mid)
            break
        elif prefix[mid] < worm:
            iz = mid+1
        else:
            dere = mid-1