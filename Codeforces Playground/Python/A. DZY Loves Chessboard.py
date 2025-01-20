colum, filas = list(map(int, input().split()))

for n in range(colum):
    tale = input()

    a = n % 2
    r = ''

    for i in range(filas):
        if tale[i] == '.':
            if i % 2 == a:
                r += 'B'
            else:
                r += 'W'
        else:
            r +=  '-'

    print(r)
