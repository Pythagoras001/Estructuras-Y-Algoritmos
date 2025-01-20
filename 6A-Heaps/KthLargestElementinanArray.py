import heapq

class Solution:
    def kthLargest(self, nums: list[int], k: int):

        if not nums or k > len(nums):
            return
        
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappushpop(heap, num)
        return(heap[0])

#######################################################

import heapq

class Solution:
    def kthLargest(self, nums: list[int], k: int):
        if not nums or k > len(nums):
            return

        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)

        return heap[0]