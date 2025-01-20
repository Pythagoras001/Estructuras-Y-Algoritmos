table = int(input())
reina = list(map(int, input().split()))
rey = list(map(int, input().split()))
objeti = list(map(int, input().split()))
r = 'NO'

distan = abs(objeti[0] - reina[0])
if objeti[1] not in [reina[1] - distan, reina[1] + distan]:
    x = sorted([rey[0], objeti[0], reina[0]])
    y = sorted([rey[1], objeti[1], reina[1]])

    if reina[0] in [x[0],x[2]] and reina[1] in [y[0],y[2]]:
        r = 'YES'

print(r)