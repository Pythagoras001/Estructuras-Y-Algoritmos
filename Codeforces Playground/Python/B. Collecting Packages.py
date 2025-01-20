veces = int(input())

for _ in range(veces):
    cant = int(input())
    lista = []

    for _ in range(cant):
        lista.append(list(map(int, input().split())))

    lista.sort()

    s = 'YES'
    r = ('R'*lista[0][0]) + ('U'*lista[0][1])
    
    for i in range(1, cant):
        if lista[i][0] >= lista[i-1][0] and lista[i][1] >= lista[i-1][1]:
            r += 'R' * (lista[i][0] - lista[i-1][0]) + 'U' * (lista[i][1] - lista[i-1][1])

        else:
            s ='NO'
    
    print(s)
    if s == 'YES':
        print(r)