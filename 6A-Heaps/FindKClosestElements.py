import heapq

class Solution:
    def kClosest(self, nums: list[int], k: int, target: int):
        heap = []
        heapq.heapify(heap)

        for num in nums:
            distance = abs(target - num)

            if len(heap) < k:
                heapq.heappush(heap, (-distance, num))
            elif distance < -heap[0][0]:
                heapq.heappushpop(heap, (-distance, num))

        return sorted(heap[i][1] for i in range(k))

solucion = Solution
solucion.kClosest(solucion, nums= [1,2,3,4,5], k= 4, target= 3)

#####################################################################

import heapq

def k_closest(nums, k, target):
  heap = []
  for num in nums:
    distance = abs(num - target)
    if len(heap) < k:
      heapq.heappush(heap, (-distance, num))
    elif distance < -heap[0][0]:
      heapq.heappushpop(heap, (-distance, num))

  distances = [pair[1] for pair in heap]
  distances.sort()
  return distances
