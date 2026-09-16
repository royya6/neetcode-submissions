class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        freq = {}
        for c in s: 
            freq[c] = freq.get(c, 0) + 1

        l = 0 
        res = []
        curr = set()

        for r in range(len(s)): 
            
            char = s[r]

            if char not in curr: 
                curr.add(char)

            freq[char] -= 1

            if not freq[char]: 
                curr.remove(char)

                if not curr:
                    res.append(r-l+1)
                    l = r+1         
        
        return res
        