for _ in range(int(input())):
    node = int(input())
    lista =  list(map(int, input().split()))

    ini = lista[0]
    d = -1
    aws = []
    rest = []

    for i in range(1, node):
        if lista[i] == ini:
            rest.append(i+1)
        else:
            aws.append([1, i+1])
            d = i+1

    if d == -1:
        print('NO')
    else:
        for i in range(len(rest)):
            aws.append([rest[i], d])

        print('YES')
        for i in range(node-1):
            print(*aws[i])
