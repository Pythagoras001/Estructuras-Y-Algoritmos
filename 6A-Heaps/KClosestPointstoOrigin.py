import heapq

puntos  = [[3,4],[2,2],[1,1],[0,0],[5,5]]
k = 3
heap = []
heapq.heapify(heap)

for i in range(len(puntos)):
    distancia = puntos[i][0]**2 + puntos[i][1]**2

    if len(heap) < k:
        heapq.heappush(heap, (-distancia, i))
    else:
        if distancia < -heap[0][0]:
            heapq.heappushpop(heap, (-distancia, i))

print([puntos[i[1]] for i in heap])

############################################################################

class Solution:
    def kClosest(self, points: list[list[int]], k: int):
            puntos  = points
            heap = []
            heapq.heapify(heap)

            for i in range(len(puntos)):
                distancia = puntos[i][0]**2 + puntos[i][1]**2

                if len(heap) < k:
                    heapq.heappush(heap, (-distancia, i))
                else:
                    if distancia < -heap[0][0]:
                        heapq.heappushpop(heap, (-distancia, i))

            return([puntos[i[1]] for i in heap])
