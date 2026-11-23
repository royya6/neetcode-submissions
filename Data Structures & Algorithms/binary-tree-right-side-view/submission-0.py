# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # go right, if null go left 
        # at each level record rightmost node
        # preorder right -> left 
        # keep track of level 
        res = []
        q = deque([root])
        depth = 0

        while q: 
            qlen = len(q)
            res.append(-1)

            for i in range(qlen): 
                node = q.popleft()
                if node:
                    if res[-1] < 0: 
                        res[-1] = node.val
                    q.append(node.right)
                    q.append(node.left)
            
            depth += 1

        return res[:-1]


        