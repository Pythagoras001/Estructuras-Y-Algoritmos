cant = int(input())

for _ in range(cant):
    a, b = map(int, input().split())

    t1 = input()
    t2 = input()
    r = 'YES'
    c = 0
    u = 'n'

    for elem in t1+t2[::-1]:
        if elem == u:
            c += 1
        u = elem

    if c > 1:
        r = 'NO'

    print(r)
    