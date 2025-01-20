veces = int(input())

for _ in range(veces):
    r = 'YES'
    ini = [0,0]

    for _ in range(int(input())):
        act = list(map(int, input().split()))
        if (act[0] - ini[0]) >= (act[1]-ini[1]) and act[1] >= ini[1]:
            ini = [act[0], act[1]]
        else:
            r = 'NO'

    print(r)