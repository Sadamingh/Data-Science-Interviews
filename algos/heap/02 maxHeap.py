import heapq

minHeap = [5,1,2,8,4,7]
heapq.heapify(minHeap * -1)

print(heapq.heappop(minHeap))
