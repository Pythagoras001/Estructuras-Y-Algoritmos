veces = int(input())

for _ in range(veces):
    cant = int(input())
    nums = list(map(int, input().split()))
    lista = list(input())

    prefix = [0] * (cant+1)
    for i in range(1, cant+1):
        prefix[i] = prefix[i-1] + nums[i-1]

    iz = 0
    dere = cant-1

    s = 0

    while iz < dere:
        if lista[iz] == 'L' and lista[dere] == 'R':
            s += prefix[dere+1] - prefix[iz]
            iz += 1
            dere -= 1
        elif lista[iz] != 'L':
            iz += 1
        else:
            dere -= 1

    print(s)
    