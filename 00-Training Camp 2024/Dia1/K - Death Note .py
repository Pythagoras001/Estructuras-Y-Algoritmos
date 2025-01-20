dias, limite = list(map(int, input().split()))
lista = list(map(int, input().split()))\

c = 0
sobra = 0

for i in range(dias):
    c += (lista[i] + sobra) // limite
    sobra = (lista[i] + sobra) % limite

    print(c, end=' ')
    c = 0