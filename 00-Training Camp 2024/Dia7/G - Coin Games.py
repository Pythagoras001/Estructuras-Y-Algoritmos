veces = int(input())

for _ in range(veces):
    num = int(input())
    repe = input().count('U')
    r = 'NO'

    if repe % 2 != 0:
        r = 'YES'

    print(r)