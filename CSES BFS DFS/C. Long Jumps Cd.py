def recur(lista):
    rs = []
    for n, arr in lista:
        dp = [0] * (n + 1)  
        maxx = 0

        for i in range(n, 0, -1):
            if i + arr[i - 1] > n:
                dp[i] = arr[i - 1]
            else:
                dp[i] = arr[i - 1] + dp[i + arr[i - 1]]
            maxx = max(maxx, dp[i])

        rs.append(maxx)

    print("\n".join(map(str, rs)))

lista = []
for _ in range(int(input()) ):
    n = int(input())
    arr = list(map(int, input().split()))
    lista.append((n, arr))

rs = recur(lista)
