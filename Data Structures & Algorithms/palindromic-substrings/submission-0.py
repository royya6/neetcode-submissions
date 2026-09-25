class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        #dp[i] = # of substrings with centre i in string 
        dp = [0]*n

        def pal(p, q): 
            # n is the position in string 
            count = 0 

            while p >= 0 and q < len(s): 
                if s[p] != s[q]: 
                    return count 
                else: 
                    count += 1
                    p -= 1
                    q += 1
            
            return count 

        for i in range(n): 
            dp[i] = pal(i, i) + pal(i, i+1)

        return sum(dp)

        