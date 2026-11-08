class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        parent = [i for i in range(n + 1)] # eg if 1 parent of 2, parent[2] = 1
        res = []

        def find(x): 
            par = parent[x]
            while par != x: 
                x = par 
                par = parent[x]
            
            return par 

        for u, v in edges: 
            upar = find(u)
            vpar = find(v)

            if upar == vpar: 
                res = [u, v]
            else: 
                parent[upar] = vpar 

            # print(u, v, res, parent)

        return res
            
