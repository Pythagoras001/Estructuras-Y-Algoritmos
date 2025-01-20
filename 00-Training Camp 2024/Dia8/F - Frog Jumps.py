veces = int(input())

for _ in range(veces):
    code = input()
    s = 1
    maxx = 0
    conta = 0

    for char in code + ' ':
        if char == 'L':
            conta += 1
        else:
            maxx = max(maxx, conta)
            conta = 0

    print(maxx+s)