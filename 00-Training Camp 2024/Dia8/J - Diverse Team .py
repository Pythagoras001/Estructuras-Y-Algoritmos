cant, grupo = list(map(int, input().split()))
lista = input().split()
dicc = dict()
c = []
apro = 0
r = 'NO'

for i in range(cant):
    if dicc.get(lista[i], 0) == 0:
        c.append(i+1)
        apro += 1
        dicc[lista[i]] = 1

        if apro == grupo:
            r = 'YES'
            break

print(r)
if r == 'YES':
    print(*c)




