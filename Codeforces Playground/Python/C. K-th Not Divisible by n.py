veces = int(input())

for _ in range(veces):
    num, index = list(map(int, input().split()))

    conju = ((index//(num-1)) * num) + (index % (num-1))
    
    if conju % num == 0:
        conju -= 1

    print(conju)