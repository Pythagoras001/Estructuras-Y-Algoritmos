n = int(input())
presidnete = list(map(int, input().split()))
miembros = list(map(int, input().split()))

puntos = {i: 0 for i in range(1, n + 1)}

for idx, code in enumerate(presidnete):
    puntos[code] += n - idx  

votoCode = [(i + 1, miembros[i]) for i in range(n)]
votoCode.sort(key=lambda x: -x[1])  

for idx, (code, _) in enumerate(votoCode):

    puntos[code] += n - idx

# print(puntos, votoCode)

result = list(puntos.items())
result.sort(key=lambda x: (-x[1], -miembros[x[0] - 1]))

for rank, (code, pts) in enumerate(result, start=1):
    print(f"{rank}. Kod{code:02d} ({pts})")
