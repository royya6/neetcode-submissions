class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network = defaultdict(list)

        for src, dst, time in times:
            network[src].append((dst, time))
        
        dists = {k: 0}
        heap = [(0, k)] # closest node 

        while heap: 

            time, node = heapq.heappop(heap)

            if time > dists[node]: continue 

            for nbr, edge_t in network[node]: 
                new_dist = time + edge_t
                
                if new_dist < dists.get(nbr, float("inf")):
                    dists[nbr] = new_dist
                    heapq.heappush(heap, (new_dist, nbr))

        
        if len(dists) < n: return -1 

        return max(dists.values())