def criva(limit):
    primos = [True] * (limit+1)
    primos[0] = primos[1] = False

    for i in range(2, int(limit**0.5)+1):
        if primos[i]:
            for n in range(i*i, limit+1, i):
                primos[n] = False

    listas = {i for i in range(limit+1) if primos[i]}
    return listas

primos = criva(int(1e6))

cant = int(input())
lista = list(map(int, input().split()))

for num in lista:
    prime = num**0.5
    r = 'NO'
    if prime**2 == num and prime in primos:
        r = 'YES'

    print(r)

