cant, dis = list(map(int, input().split()))
ubica = list(map(int, input().split()))
t = 2

for i in range(1, cant):
    a = ((abs(ubica[i-1] - ubica[i])) - dis*2) + 1

    if a > 1:
        t += 2
    elif a > 0:
        t += 1

print(t)

