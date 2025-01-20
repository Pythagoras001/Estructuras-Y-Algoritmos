import heapq

lista = list(map(int, input().split()))

heap = lista[:3]

heapq.heapify(heap)

for num in lista[3:]:
    if num > heap[0]: #Comparamos si num es mayor que la raiz
        heapq.heappop(heap) #Sacamos la raiz para remplazarla por un num mayor
        heapq.heappush(heap, num) #Metemos num dentro del monto y se organiza

print(heap)

