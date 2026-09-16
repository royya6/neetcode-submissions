class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []

        def dfs(r, c, reach): 
            if (r,c) in reach: 
                return 

            reach.add((r, c))
            adj = [(r+1, c),(r-1, c), (r, c+1), (r, c-1)]

            for coord in adj: 
                if (0 <= coord[0] < ROWS and 
                    0 <= coord[1] < COLS and 
                    heights[coord[0]][coord[1]] >= heights[r][c]): 
                    
                    dfs(coord[0], coord[1], reach)

        # top and bottom border
        for i in range(COLS): 
            dfs(0, i, pac)
            dfs(ROWS-1, i, atl)
        
        #left and right border 
        for j in range(ROWS): 
            dfs(j, 0, pac)
            dfs(j, COLS-1, atl)

        return [[r, c] for r, c in pac & atl]


        