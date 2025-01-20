num = int(input())

if num == 1:
    print(1)
elif num < 4:
    print('NO SOLUTION')
else:
    if num == 4:
        print(2,4,1,3)
    else:
        print(*[i for i in range(1, num+1, 2)] + [i for i in range(2, num+1, 2)])