class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i in stones:
            heap.append(-i)
        heapq.heapify(heap)
        while len(heap)>1:
            v1=heapq.heappop(heap)
            v2=heapq.heappop(heap)
            diff = abs(v2-v1)
            if diff==0:
                pass
            else:
                heapq.heappush(heap, -diff)
        if len(heap)>0:
            return heap[0]*-1
        else:
            return 0
            
                
        