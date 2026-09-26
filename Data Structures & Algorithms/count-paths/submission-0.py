class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # dp[i][j] = num of ways to reach grid[i][j]
        dp = [[0]*n]*m

        # initialise first row and col 
        dp[0] = [1]*n
        for r in dp:
            r[0] = 1

        # print(dp)
        
        for i in range(1, m): 
            for j in range(1, n): 
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # print(dp)
        

        return dp[m-1][n-1]