# Recibimos la entrada
cant, k = list(map(int, input().split()))
alturas = list(map(int, input().split()))

# Creamos el dp
dp = [0]*cant

# Llenamos el dp
# dp[n] = min(costoActual(altura[n]-altura[n+1..]) + dp[n+1...])

for n in range(cant-2, -1, -1):
    op = float('inf')
    for i in range(1, min(k+1, cant-(n))):

        op = min(op, abs(alturas[n] - alturas[n+i]) + dp[n+i])
    dp[n] = op

print(dp[0])
