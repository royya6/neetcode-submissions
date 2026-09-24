class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check complete 
        if n != len(edges)+1: return False 

        par = list(range(n))
        rank = [1]*n 

        found = []

        def find(x): 
            res = x 

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            
            return res 

        def union(u, v): 
            x, y = find(u), find(v)
            if x == y: return False 

            if rank[x] >= rank[y]: 
                rank[x] += rank[y]
                par[y] = par[x]
            else: 
                rank[y] += rank[x]
                par[x] = par[y]
            
            return True 


        for u, v in edges: 
            if not union(u, v): return False

        return True
                


            



        
