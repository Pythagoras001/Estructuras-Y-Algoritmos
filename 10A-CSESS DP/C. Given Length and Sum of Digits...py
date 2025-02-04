a, b = map(int, input().split())

if 9*a < b or (b == 0 and a > 1):
    print(-1, -1)

else:
    s = [0]*a

    for i in range(a):
        if b >= 9:
            s[i] = 9
            b -= 9
            continue
        
        s[i] = b
        break

    s2 = s[::-1]

    if s2[0] == 0:
        for i in range(a):
            if s2[i] != 0:
                s2[i] -= 1
                s2[0] += 1
                break

    print(''.join(list(map(str, s2))), ''.join(list(map(str, s))))
