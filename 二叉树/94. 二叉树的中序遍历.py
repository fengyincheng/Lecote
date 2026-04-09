# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            ans.append(node.val) #为什么只添加根节点呢？
            dfs(node.right)
            """
            树递归里“根节点”是相对概念。

            对于每次递归而言，

            当前 node 就是当前子树的根。
            """
        ans=[]
        dfs(root)
        return ans


            