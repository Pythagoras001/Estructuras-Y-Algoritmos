veces = int(input())

for _ in range(veces):
    num = int(input())
    l = []
    r = 'NO'

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            l.append(i)
            num = num // i
            break

    if len(l) > 0:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0 and i != l[0] and num // i != l[0] and num // i != i:
                l.append(i)
                l.append(num // i)
                r = 'YES'
                break
    
    print(r)
    if r == 'YES':
        print(*l)
    