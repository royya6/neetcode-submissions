class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check complete 
        if n < len(edges)+1: return False 

        found = set()

        adj = [[] for _ in range(n)]
        for u, v in edges: 
            adj[u].append(v)
            adj[v].append(u)

        def dfs(start, parent): 
            # cycle 
            if start in found: return False 

            found.add(start)
            for nbr in adj[start]: 
                if nbr == parent: 
                    continue 
                if not dfs(nbr, start): 
                    return False 

            return True 

        return dfs(0, -1) and len(found) == n 
