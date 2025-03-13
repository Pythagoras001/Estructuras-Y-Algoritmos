cant = int(input())
lista = sorted(list(map(int, input().split())))

c = 0
rep = dict()

for elem in lista: rep[elem] = rep.get(elem, 0) + 1
valores = sorted(list(rep.keys()))

dp = [0]*len(rep.keys())
dp[0] = rep[valores[0]] * valores[0]
maxx = [dp[0], 0]

for i in range(1, len(valores)):

    if valores[i-1] == valores[i] - 1:
        suma = maxx[1]
    else: suma = maxx[0]

    dp[i] = ( valores[i] * rep[valores[i]] ) + suma

    maxx[1] = maxx[0]
    if dp[i] > maxx[0]:
        maxx[0] = dp[i]

print(max(dp))