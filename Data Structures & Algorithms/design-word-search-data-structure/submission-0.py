class DictNode: 
    def __init__(self): 
        self.children = {}
        self.end = False 

class WordDictionary:

    def __init__(self):
        self.root = DictNode()

    def addWord(self, word: str) -> None:
        node = self.root 

        for char in word: 
            if char not in node.children: 
                node.children[char] = DictNode()
            
            node = node.children[char]
        
        node.end = True 

    def search(self, word: str) -> bool:
        
        def dfs(i, root): 
            curr = root

            for j in range(i, len(word)): 
                c = word[j]
                if c == ".": 
                    for child in curr.children.values():
                        if dfs(j + 1, child): return True 

                    return False 
                    
                else: 
                    if c not in curr.children: 
                        return False 
                    
                    curr = curr.children[c]
            
            return curr.end 

        return dfs(0, self.root)
        
