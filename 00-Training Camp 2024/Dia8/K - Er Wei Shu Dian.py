veces = int(input())
x = dict()
y = dict()
ubica = []

def diccionar(index, dicc):
    if index not in dicc:
        dicc[index] = 1
    else:
        dicc[index] += 1
    return dicc

for _ in range(veces):
    ubica.append(list(map(int, input().split()))[::-1])

ubica = sorted(ubica)

s = 0
a = 0

for i in range(veces):
    if i > 0 and ubica[i] == ubica[i-1]:
        s += a
    else:
        s += i - (x.get(ubica[i][1], 0) + y.get(ubica[i][0], 0))
        a = i - (x.get(ubica[i][1], 0) + y.get(ubica[i][0], 0))

    diccionar(ubica[i][1], x)
    diccionar(ubica[i][0], y)

print(s)