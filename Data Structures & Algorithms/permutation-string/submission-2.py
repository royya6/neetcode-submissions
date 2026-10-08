class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def getFreq(s): 
            hm = {}
            for c in s: 
                hm[c] = hm.get(c, 0) + 1 

            return hm 


        # hashmap of the chars of s1 
        s1chars = getFreq(s1)

        n = len(s1)

        for l in range(len(s2)-n+1): 
            currString = s2[l: l+n]
            print(currString)
            if getFreq(currString) == s1chars: 
                return True

        return False 

        