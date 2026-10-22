class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        HEIGHT, WIDTH = len(grid), len(grid[0])
        q = deque()

        # travel from chests to land, marking min distance until reaching a value smaller 

        for r in range(HEIGHT): 
            for c in range(WIDTH): 
                if grid[r][c] == 0: 
                    q.append((r, c))
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while q: 
            r, c = q.popleft()
            dist = grid[r][c] + 1

            for x, y in directions: 
                nr, nc = r + x, c + y

                if nr < 0 or nr >= HEIGHT or nc < 0 or nc >= WIDTH: 
                    continue 

                if grid[nr][nc] <= dist: 
                    continue 

                grid[nr][nc] = dist 
                q.append((nr, nc))






        