class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if s[0] == "0": return 0 
        if n == 1: return 1 

        # list of valid digits
        digits = [str(i) for i in range(1, 27)]

        #dp[i] = number of letters that can be made with the first i letters 
        dp = [0] * (n + 1)  
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1): 
            print(s[i-1:i+1])
            if 10 <= int(s[i-2:i]) <= 26: 
                dp[i] += dp[i-2]
            if s[i-1] != "0": 
                dp[i] += dp[i-1]

        return dp[n]


        