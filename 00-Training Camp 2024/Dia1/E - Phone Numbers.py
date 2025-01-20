cant = int(input())
lista = input()

nums = 0
ochos = 0

for i in range(cant):
    if lista[i] != '8':
        nums += 1
    else:
        ochos += 1

total = min(ochos, (nums//10))
ochos -= total
nums -= total*10

while ochos + nums >= 11 and ochos > 0:
    ochos -= 11-nums
    nums = 0
    total += 1

print(total)

