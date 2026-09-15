class Node: 
    def __init__(self): 
        self.children = {}
        self.is_end = False 

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word: 
            child = node.children.get(char)

            if child is None: 
                child = Node()
                node.children[char] = child 
            
            node = child
        
        node.is_end = True 
                

    def search(self, word: str) -> bool:
        node = self.root
        for char in word: 
            node = node.children.get(char)
            if node is None: return False 
        
        return node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix: 
            node = node.children.get(char)
            if node is None: return False 
        
        return True
        
        