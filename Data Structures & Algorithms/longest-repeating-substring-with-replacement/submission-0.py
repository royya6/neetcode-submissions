class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        seen = {}
        l = 0
        max_freq = 0  
        longest = 0 

        for r in range(len(s)): 
            seen[s[r]] = seen.get(s[r], 0) + 1
            max_freq = max(max_freq, seen[s[r]])

            while (r - l + 1) - max_freq > k: 
                seen[s[l]] -= 1
                l += 1
            
            longest = max(longest, (r-l+1))

        return longest




        