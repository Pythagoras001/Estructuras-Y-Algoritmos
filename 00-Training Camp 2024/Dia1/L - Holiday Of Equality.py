num = int(input())
lista = list(map(int, input().split()))
print(max(lista)*num - sum(lista))
