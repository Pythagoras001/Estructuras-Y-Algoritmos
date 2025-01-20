veces = int(input())

for _ in range(veces):
    tama, x, y = list(map(int, input().split()))

    distaMax = y-x
    div = 1

    for i in range(1, distaMax+1): 
        if distaMax % i == 0 and distaMax // i <= tama-1:
            div = i
            break
    
    r = []

    for i in range(y, 0, -div):
        r.append(i)
        tama -= 1
        if tama == 0:
            break

    ulti = r[0]

    for i in range(tama):
        r.append(ulti+div)
        ulti += div

    print(*r)