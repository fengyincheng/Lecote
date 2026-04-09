# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node,depth):
            if node is None:
                return
            depth +=1
            nonlocal ans
            ans = max(ans,depth)
            dfs(node.left,depth) #看不懂，什么意思啊
            dfs(node.right,depth)
        dfs(root,0)
        return ans 