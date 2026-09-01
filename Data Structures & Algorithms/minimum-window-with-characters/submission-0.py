class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # initialise target freq hashmap 
        target = {}
        for ch in t: 
            target[ch] = target.get(ch, 0) + 1

        print(target)
        
        curr = {}
        formed = 0 
        required = len(target)
        l = 0 

        res = [-1, -1]
        resLen = float("infinity")

        for r in range(len(s)): 
            curr[s[r]] = curr.get(s[r], 0) + 1

            
            if s[r] in target and curr[s[r]] == target[s[r]]: 
                formed += 1

                # print(s[r], curr[s[r]], target[s[r]])

            while formed == required: 
                if (r-l+1) < resLen: 
                    res = [l, r]
                    resLen = r - l + 1

                curr[s[l]] -= 1
                if s[l] in target and curr[s[l]] < target[s[l]]: 
                    formed -= 1
                
                l += 1
            
        l, r = res            
        return s[l: r+1] if resLen != float("infinity") else ""
