
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = {c: set() for w in words for c in w}

        # build graph
        for i in range(len(words)-1): 
            w1, w2 = words[i], words[i+1] 
            minLen = min(len(w1), len(w2))
            
            # check not invalid 
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: 
                return ""

            for j in range(minLen): 
                if w1[j] != w2[j]: 
                    adj[w1[j]].add(w2[j])
                    break 
            

        print(adj)

        # dfs 
        visited = {}
        res = []

        def dfs(char): 
            if char in visited: 
                return visited[char]
            
            visited[char] = True 

            for nbr in adj[char]: 
                if dfs(nbr): 
                    return True 
            
            visited[char] = False 
            
            # exit node 
            res.append(char)

        for char in adj: 
            if dfs(char): 
                return ""
        
        res.reverse()
        return "".join(res)



        

        return "aaa"

        