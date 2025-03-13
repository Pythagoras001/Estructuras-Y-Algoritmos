cant = int(input())

lista1 = list(map(int, input().split()))[::-1]
lista2 = list(map(int, input().split()))[::-1]

dp = [[0, 0] for _ in range(cant)]
dp[0] = [lista1[0], lista2[0]]

if cant >= 2:
    dp[1] = [lista1[1] + dp[0][1], lista2[1] +  dp[0][0]]
    
    for i in range(2, cant):
        dp[i] = [lista1[i] + max(dp[i-1][1], dp[i-2][1]) ,lista2[i] + max(dp[i-1][0], dp[i-2][0])]
        
print(max(dp[-1]))