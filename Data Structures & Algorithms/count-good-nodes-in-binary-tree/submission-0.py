# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, cur_max): 

            if not node: 
                return 0
            
            print(node.val)
            count = 1 if node.val >= cur_max else 0
            cur_max = max(cur_max, node.val)

            return (count + dfs(node.left, cur_max) + dfs(node.right, cur_max))

        return dfs(root, root.val)
        