numper, numapart, tole = list(map(int, input().split()))
persons = sorted(list(map(int, input().split())), reverse=True)
aparts = sorted(list(map(int, input().split())), reverse=True)

p = 0
a = 0
c = 0

while True:
    if abs(persons[p] - aparts[a]) <= tole:
        c += 1
        p += 1
        a += 1
    elif persons[p] > aparts[a]:
        p += 1
    else:
        a += 1
    
    if a == numapart or p == numper:
        break

print(c)