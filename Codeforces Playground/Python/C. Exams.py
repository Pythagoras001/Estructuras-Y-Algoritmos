days = int(input())
date = []

for _ in range(days):
    date.append(list(map(int, input().split())))

date.sort()

u = date[0][1]

for i in range(1, days):
    if date[i][1] >= u:
        u = date[i][1]
        continue
    
    u = date[i][0]

print(u)
