import heapq 

class MedianFinder:

    def __init__(self):
        # have a max heap (bottom half of nums) and a min heap (top half)
        self.maxheap = []
        self.minheap = []
        

    def addNum(self, num):
        heapq.heappush(self.maxheap, -num)

        heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        return (-self.maxheap[0] + self.minheap[0]) / 2

        
        