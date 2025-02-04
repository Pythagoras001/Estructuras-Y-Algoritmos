# Recibimos la entrada
cant = int(input())
alturas = list(map(int, input().split()))

# Creamos el dp
dp = [0]*cant

# Llenamos el dp con la configuracion
# dp[n] = min(costoActual(altura[n]-altura[n+1]) + dp[n+1], costoActual(altura[n]-altura[n+2]) + dp[n+2 ]) 
for n in range(cant-2, -1, -1):
    op = abs(alturas[n]-alturas[n+1]) + dp[n+1]

    if n != cant-2:
        op = min(op, abs(alturas[n]-alturas[n+2]) + dp[n+2])

    dp[n] = op


print(dp[0])