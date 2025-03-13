cant = int(input())

valores = []

for _ in range(cant):
    valores.append(int(input()))

dp = [0]*max(valores)

dp[0] = 1

for i in range(1, max(valores)):
    suma = 0
    num = str(i+1)
    if len(num) >= 2:
        for digit in num:
            suma += int(digit)
    else:
        suma += i + 1

    dp[i] = dp[i-1] + suma

for ind in valores:
    print(dp[ind-1])