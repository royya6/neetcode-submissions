class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs: 
            n = len(s)
            res += [str(n), '#',s]

        # print(res)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        length = len(s)
        i = 0 
        res = []

        while i < length :
            numStr = ""
            while s[i] != '#': 
                numStr += s[i]
                i += 1
            
            num = int(numStr)
            # print(num)
            i += 1

            word = ""
            lim = i + num
            while i < lim: 
                word += s[i]
                i += 1
                # print(word)

            res.append(word)


        return res 
            
