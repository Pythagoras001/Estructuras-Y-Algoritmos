cant = int(input())
grupos = list(map(int, input().split()))
dicc = dict()

for num in grupos:
    if num not in dicc:
        dicc[num] = 1
    else:
        dicc[num] += 1

r = dicc.get(4, 0) + dicc.get(3, 0)

if 1 in dicc:
    dicc[1] -= dicc.get(3, 0)
    if dicc[1] < 0:
        dicc[1] = 0

r += ((dicc.get(2, 0)*2) + dicc.get(1, 0)) // 4
if ((dicc.get(2, 0)*2) + dicc.get(1, 0)) % 4 != 0:
    r += 1

print(r)