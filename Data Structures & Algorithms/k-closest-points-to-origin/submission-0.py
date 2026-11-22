import math 

class Solution:
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(x, y): 
            return math.sqrt(x**2 + y**2)

        maxheap = [] 

        for x, y in points: 
            curr_dist = dist(x, y)
            heapq.heappush(maxheap, (-curr_dist, [x, y]))

            if len(maxheap) > k: 
                heapq.heappop(maxheap)

        return [p for _, p in maxheap]
            


