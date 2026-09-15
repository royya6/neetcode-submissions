class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.idx = -1
        self.refs = 0 
    
    def addWord(self, word, i): 
        curr = self 
        curr.refs += 1
        
        for char in word: 
            if char not in curr.children: 
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
            curr.refs += 1 
        
        curr.idx = i 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create trie 
        root = TrieNode()
        for i in range(len(words)): 
            root.addWord(words[i], i)
        
        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, node): 

            if (r<0 or c<0 or r>=ROWS or c>= COLS or board[r][c] == '#'
               or not node.children.get(board[r][c])): 
                return 0

            tmp = board[r][c]
            board[r][c] = '#'
            prev = node 
            node = node.children[tmp]
            found = 0 
            if node.idx != -1:
                res.append(words[node.idx])
                node.idx = -1 
                found += 1

            found += dfs(r + 1, c, node)
            found += dfs(r - 1, c, node)
            found += dfs(r, c + 1, node)
            found += dfs(r, c - 1, node)

            #backtrack 
            board[r][c] = tmp
            node.refs -= found 
            if not node.refs: 
                prev.children[tmp] = None 

            return found
        
        for i in range(ROWS): 
            for j in range(COLS): 
                root.refs -= dfs(i, j, root)

        return res
        