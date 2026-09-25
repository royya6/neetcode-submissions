class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # DSU 
        par = list(range(n))
        components = n 

        def find(x): 
            res = x
            while res != par[res]: 
                res = par[res]
                par[res] = par[par[res]]
            
            return res 

        def union(u, v): 
            nonlocal components
            pu, pv = find(u), find(v)

            # cycle
            if pu == pv:
                return 
            
            par[pu] = pv 
            components -= 1
            return 

        for u, v in edges: 
            union(u, v)
        
        return components 
            
            