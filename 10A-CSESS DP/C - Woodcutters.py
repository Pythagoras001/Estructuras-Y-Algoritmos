cant = int(input())

arboles = []

for _ in range(cant):
    arboles.append(list(map(int, input().split())))

talaDer = [0]*cant

dp = [[0,0,0] for _ in range(cant)]
dp[0] = [1, 0, 0]

if cant >= 2:
    if arboles[0][0] + arboles[0][1] < arboles[1][0]:
        dp[0][2] = 1
        talaDer[0] = 1

for i in range(1, cant-1):
    
    disAc = arboles[i][0] - arboles[i][1]
    disPas = arboles[i-1][0] + arboles[i-1][1]

    if arboles[i][0] - arboles[i][1] > arboles[i-1][0]:
        if not talaDer[i-1] or disAc > disPas:
            dp[i][0] = max(dp[i-1]) + 1
        else: 
            dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]-1)+1
    else:
        dp[i][0] = max(dp[i-1])

    dp[i][1] = max(dp[i-1])

    if arboles[i][0] + arboles[i][1] < arboles[i+1][0]:
        dp[i][2] = max(dp[i-1]) + 1
        talaDer[i] = 1
    else:
        dp[i][2] = max(dp[i-1])

if cant >= 2:
    print(max(dp[cant-2])+1)
else: print(max(dp[cant-2]))

    
    
    

