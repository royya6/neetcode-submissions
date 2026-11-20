class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False 

        # build char map 
        charmap = Counter(s)

        charcount = 0 

        for char in t: 
            # print(charmap)
            if charmap[char] > 0: 
                charmap[char] -= 1
                charcount += 1

        return charcount == len(t)



         

        