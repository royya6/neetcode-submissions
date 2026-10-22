class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        HEIGHT, WIDTH = len(grid), len(grid[0])

        def dfs(i, j): 
            if i < 0 or i >= HEIGHT or j < 0 or j >= WIDTH:
                return 0

            if grid[i][j] == 0 or grid[i][j] == -1: 
                return 0

            grid [i][j] = -1

            size = 1 + dfs(i-1, j) + dfs(i, j+1) + dfs(i+1, j) + dfs(i, j-1)

            return size 

        maxArea = 0

        for r in range(HEIGHT):
            for c in range(WIDTH):
                area = dfs(r, c)
                maxArea = max(area, maxArea)

        return maxArea
        