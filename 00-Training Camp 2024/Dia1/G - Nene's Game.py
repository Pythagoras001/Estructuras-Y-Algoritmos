veces = int(input())

for _ in range(veces):
    k, q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    n = list(map(int, input().split()))

    corte = min(a)
    r = []

    for num in n:
        if num >= corte:
            r.append(corte-1)
        else:
            r.append(num)

    print(*r)