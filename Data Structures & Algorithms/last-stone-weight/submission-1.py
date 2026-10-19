class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones: 
            heapq.heappush(maxHeap, -stone)
        
        while len(maxHeap) > 1: 
            s1 = -heapq.heappop(maxHeap)
            s2 = -heapq.heappop(maxHeap)

            if s1 == s2: 
                continue 
            
            if s1 < s2: 
                heapq.heappush(maxHeap, s1-s2)
            else: 
                heapq.heappush(maxHeap, s2-s1)
            
        return 0 if len(maxHeap) == 0 else -maxHeap[0]

        