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
            j = i 
            while s[i] != '#': 
                i += 1
            
            num = int(s[j:i])
            # print(num)
            i += 1

            word = s[i:i+num]

            i += num

            res.append(word)


        return res 
            
