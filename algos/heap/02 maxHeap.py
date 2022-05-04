import heapq

maxHeap = [5,1,2,8,4,7]

maxHeap = [-x for x in maxHeap]
heapq.heapify(maxHeap)

print(heapq.heappop(maxHeap) * -1)
