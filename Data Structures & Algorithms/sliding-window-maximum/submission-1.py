class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        maxheap = []

        for r, val in enumerate(nums): 

            heapq.heappush(maxheap, (-val, r)) 

            l = r - k + 1
            while maxheap[0][1] < l: 
                heapq.heappop(maxheap)
            
            if r >= k - 1: 
                res.append(-maxheap[0][0])

        return res

        
        
            