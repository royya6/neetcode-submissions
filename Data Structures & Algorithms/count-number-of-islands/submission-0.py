class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # union the 1s and # when visited 
        ROWS, COLS = len(grid), len(grid[0])
        res = 0 

        def island(r, c): 
            # find island and increment res 
            if (r<0 or c<0 or r>=ROWS or c>= COLS or 
                grid[r][c] == "0"): 
                return

            grid[r][c] = "0"
            island(r+1, c)
            island(r-1, c) 
            island(r, c+1)
            island(r, c-1)

        for i in range(ROWS): 
            for j in range(COLS): 
                if grid[i][j] == "1": 
                    island(i, j)
                    res += 1
        
        return res



            