class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # dp[i] = longest palindrom with centre i 
        res = ""
        n = len(s) 

        def expand(l, r): 
            nonlocal res

            while (l >= 0 and r < n and s[l]==s[r]): 
                if  r-l+1 > len(res): 
                    res = s[l: r+1]
                
                r += 1
                l -= 1

        
        for i in range(n): 
            expand(i, i)
            expand(i, i+1)

        return res