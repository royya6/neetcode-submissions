class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        visited = [False] * n 
        minheap = [] # [(dist, idx)]
        res = 0 
        
        heapq.heappush(minheap, (0,0))

        while minheap: 
            
            weight, idx = heapq.heappop(minheap)

            if visited[idx]: 
                continue 
            
            res += weight 
            visited[idx] = True 

            for i in range(n): 
                if not visited[i]:
                    heapq.heappush(minheap, (manhattan(points[i], points[idx]), i))

            # print(idx, res)

        return res 



        