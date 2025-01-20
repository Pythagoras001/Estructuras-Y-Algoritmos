apples = list(map(int, input().split()))
total = int(input())

iz = 1
der = max(apples)
minn = max(apples)

while iz <= der:
    mid = (iz + der) // 2
    time = 0

    for i in range(len(apples)):
        time += apples[i] // mid
        if (apples[i] // mid) - (apples[i] / mid) != 0:
            time += 1

    if time > total:
        iz = mid + 1
    else:
        minn = min(minn, mid)
        der = mid - 1

print(minn) 

################################################################

class Solution:
    def minHarvestRate(self, apples: list[int], h: int):
        def time_taken(rate):
            time = 0
            for apple in apples:
                time += (apple + rate - 1) // rate
            return time

        left, right = 1, max(apples)
        while left < right:
            mid = (left + right) // 2
            if time_taken(mid) > h:
                left = mid + 1
            else:
                right = mid
                
        return left