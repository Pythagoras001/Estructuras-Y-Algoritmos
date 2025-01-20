veces = int(input())

for _ in range(veces):
    num = int(input())
    code = list(map(int, input().split()))
    r ='Mike'
    minn = float('inf')
    index = 0

    if num > 1 and num % 2 == 0:
        for i in range(num):
            if code[i] < minn:
                minn = code[i]
                index = i+1

        if index % 2 != 0:
            r = 'Joe'

    print(r)