veces = int(input())

for _ in range(veces):
    b, a = list(map(int, input().split()))
    barcos = list(map(int, input().split()))

    i = 0
    f = b-1

    di = (a // 2) + (a % 2)
    dd = a // 2

    c = 0

    while i <= f and di + dd > 0:
        
        if di > 0:
            di -= barcos[i]
            if di >= 0:
                i += 1
                c += 1
            else:
                barcos[i] = -di
                di = 0
        
        
        if dd > 0:
            dd -= barcos[f]
            if dd >= 0:
                f -= 1
                c += 1
            else:
                barcos[f] = -dd
                dd = 0

    if f < i:
        print(b)
    else:
        print(c)
