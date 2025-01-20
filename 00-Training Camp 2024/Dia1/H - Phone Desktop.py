veces = int(input())

for _ in range(veces):
    a, b = list(map(int, input().split()))

    r = (b//2)
    a -= r*7 

    if b % 2 != 0:
        r += 1
        a -= 11
    
    if a > 0:
        r += (a//15)
        if a % 15 != 0:
            r += 1
    
    print(r)