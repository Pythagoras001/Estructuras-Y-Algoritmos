# Recibimos la entrada
cant = int(input())

dias = []
for _ in range(cant):
    dias.append(list(map(int, input().split())))

# Creamos el dp
dp = [[0, 0, 0] for _ in range(cant)]

# Llenamos el dp
# dp[n] = dia[ind][n] + (max[ind-1]-{n})

dp[0] = dias[0]

for y in range(1, cant):
    for x in range(3):
        if x == 0:
            r = max(dp[y-1][1:])
        elif x == 2:
            r = max(dp[y-1][:2])
        else:
            r = max(dp[y-1][::2])
    
        dp[y][x] = dias[y][x] + r

print(max(dp[-1]))