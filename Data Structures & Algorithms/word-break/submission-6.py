class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)

        # dp[i] = if s[:i] can be split into words
        dp = [False] * (n + 1) 
        dp[0] = True  

        l = 0
        for r in range(1, n+1): 
            
            for l in range(r):
                if dp[l] and s[l:r] in words: 
                    dp[r] = True 
                    break
        

        return dp[n] 